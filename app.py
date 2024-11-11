import json
import os
from time import sleep

from flask import Flask, request, jsonify
from twikit import Client

from llm import is_tweet_beneficial, is_tech_job_tweet_beneficial

interacted_tweets = set()
app = Flask(__name__)

client = Client('en-US')

cookies_json = os.getenv('COOKIES_JSON')
if cookies_json:
    cookies = json.loads(cookies_json)
    client.set_cookies(cookies)
else:
    print("Cookies not found in the environment variable!")


def get_tweet_data(tweet):
    return {
        'id': tweet.id,
        'text': tweet.text,
        'user': {
            'id': tweet.user.id,
            'username': tweet.user.screen_name
        },
    }


@app.route('/')
async def hello_world():
    return 'Hello World!'


@app.route('/post_tweet', methods=['POST'])
async def post_tweet():
    data = request.json
    tweet_text = data.get("tweet", "")

    if not tweet_text or tweet_text.strip() == "":
        return jsonify({"error": "No tweet text provided"}), 400

    try:
        await client.create_tweet(text=tweet_text)
        return jsonify({"message": "Tweet posted successfully!"}), 200

    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500


@app.route('/interact/<keyword>')
@app.route('/interact_for_job/<keyword>')
async def interact_with_tweet(keyword):
    route_path = request.path
    search_results = await client.search_tweet(keyword, 'Latest', 20)

    if not search_results:
        return {'error': 'No tweets found with the given keyword'}, 404

    tweets_data = []
    liked_tweets = []
    commented_tweets = []
    retweeted_tweets = []
    bookmarked_tweets = []

    for tweet in search_results:
        tweets_data.append(get_tweet_data(tweet))

    for tweet in search_results:
        try:
            if tweet.id in interacted_tweets:
                continue

            interacted_tweets.add(tweet.id)
            tweet_data = get_tweet_data(tweet)

            if route_path.startswith("/interact_for_job"):
                tweet_information = is_tech_job_tweet_beneficial(tweet.text)
            else:
                tweet_information = is_tweet_beneficial(tweet.text)

            if not tweet_information:
                continue

            if not tweet_information["beneficial_for_engagement"]:
                continue

            if tweet_information["like_tweet"] and not tweet.favorited:
                await tweet.favorite()
                liked_tweets.append(tweet_data)

                if tweet_information["comment_on_tweet"]:
                    sleep(60)
                    await tweet.reply(tweet_information["comment_text"])
                    tweet_data["comment"] = tweet_information["comment_text"]
                    commented_tweets.append(tweet_data)
                    print(f"Replied to tweet: {tweet.text}\n\n")

                if tweet_information["retweet_tweet"]:
                    sleep(10)
                    await tweet.retweet()
                    retweeted_tweets.append(tweet_data)
                    print(f"Retweeted tweet: {tweet.text}\n\n")

                if tweet_information["bookmark_tweet"]:
                    await tweet.bookmark()
                    bookmarked_tweets.append(tweet_data)
                    print(f"Bookmarked tweet: {tweet.text}\n\n")

                sleep(60)

            if tweet_information["emails"]:
                print(f"\n\n**Emails: {tweet_information['emails']}**\n\n")

        except Exception as e:
            print(e)

    return jsonify(
        {"tweets": tweets_data, "liked": liked_tweets, "commented": commented_tweets, "retweeted": retweeted_tweets,
         "bookmarked": bookmarked_tweets}), 200


if __name__ == '__main__':
    app.run(debug=True)
