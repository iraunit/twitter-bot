Here’s a basic README file template for your Flask Twitter bot project. It covers project setup, usage, and functionality.

Twitter Engagement Bot for Shypt Solution

This project is a Twitter engagement bot built using Flask, designed to promote engagement for Shypt Solution’s tech-focused products such as CodingKaro, Get Link, and more. The bot searches Twitter for tech-related tweets, interacts with relevant posts, and posts updates on job listings, contests, and tech blogs to increase visibility.

Features

	•	Automated Posting: Posts updates about job listings, contests, and tech blogs to engage with a tech audience.
	•	Smart Engagement: Finds tweets based on keywords like #hiring, #referral, leetcode, codeforces, tech jobs, etc., and interacts with them if they are beneficial for engagement.
	•	Intelligent Filtering: Filters tweets based on specific criteria (e.g., tech job listings for freshers with less than 1 year of experience) and only engages with genuine posts.
	•	Dynamic Engagement Decision: Uses AI to determine if liking or commenting on a tweet would benefit engagement and suggests an appropriate comment when applicable.

Setup and Installation

	1.	Clone the Repository:

git clone https://github.com/iraunit/twitter-bot
cd twitter-engagement-bot


	2.	Install Requirements:
Install the necessary dependencies by running:

pip install -r requirements.txt


	3.	Set Environment Variables:
Configure your environment variables in a .env file:

GEMINI_API_KEY=your_api_key
OLLAMA_URL=your_ollama_url
OLLAMA_API_KEY=your_ollama_api_key
COOKIES_JSON=your_twitter_cookies_json


	4.	Run the Application:
To start the Flask app, run:

python app.py

The app will be accessible at http://0.0.0.0:5000.

Endpoints

1. POST /post_tweet

This endpoint allows you to post a tweet with a specified text.
	•	Method: POST
	•	Request Body:

{
  "tweet": "Your tweet text here"
}


	•	Response:
	•	200 OK: Tweet posted successfully.
	•	400 Bad Request: No tweet text provided.
	•	500 Internal Server Error: An error occurred while posting the tweet.
	•	Example Request:

curl -X POST http://localhost:5000/post_tweet -H "Content-Type: application/json" -d '{"tweet": "Hello, world!"}'

2. GET /interact/<keyword> and /interact_for_job/<keyword>

These endpoints search for tweets containing the specified keyword and interact with relevant tweets based on certain criteria. The /interact_for_job/<keyword> endpoint specifically looks for job-related tweets, while /interact/<keyword> is more general.
	•	Method: GET
	•	Parameters:
	•	keyword: A string keyword to search for in tweets.
	•	Route Differences:
	•	/interact/<keyword>: General engagement with tweets based on tech and coding relevance.
	•	/interact_for_job/<keyword>: Engagement specifically for job-related tweets in tech.
	•	Response:
	•	200 OK: Returns a list of tweets and the engagement actions taken on each.
	•	404 Not Found: No tweets found with the specified keyword.
	•	Response Format:

{
  "tweets": [
    {
      "tweet_id": "123456",
      "text": "Example tweet text",
      "comment": "Example comment if commented"
    }
  ],
  "liked": [ /* List of liked tweets */ ],
  "commented": [ /* List of commented tweets */ ],
  "retweeted": [ /* List of retweeted tweets */ ],
  "bookmarked": [ /* List of bookmarked tweets */ ]
}

Key Components in the Code

	1.	Tweet Search and Filtering:
	•	Searches for up to 20 latest tweets containing the specified keyword.
	•	Collects the tweet data and prepares it for analysis.
	2.	Engagement Decision:
	•	For /interact_for_job, the is_tech_job_tweet_beneficial function filters tweets to identify genuine, high-paying tech job listings for freshers and those with less than 1 year of experience.
	•	For /interact, the is_tweet_beneficial function assesses if engaging with a tweet would benefit the tech-focused account.
	3.	Engagement Actions:
	•	Like: If engagement is beneficial and the tweet is not already liked.
	•	Comment: Adds a comment to relevant tweets based on the provided analysis, with a delay for natural engagement.
	•	Retweet: Retweets the tweet if determined beneficial.
	•	Bookmark: Bookmarks the tweet if deemed beneficial.

Example Usage

	1.	Posting a Tweet:

curl -X POST http://localhost:5000/post_tweet -H "Content-Type: application/json" -d '{"tweet": "New coding resources available on CodingKaro!"}'


	2.	Interacting with Job-Related Tweets:

curl -X GET http://localhost:5000/interact_for_job/hiring


	3.	Interacting with General Tech Tweets:

curl -X GET http://localhost:5000/interact/leetcode

Error Handling

	•	If a tweet interaction fails (due to rate limits or API errors), the error message is logged, and the bot continues with the next tweet.
	•	If no tweets are found with the specified keyword, the API returns a 404 response.

Additional Notes

	•	Rate Limiting: The bot includes delays between actions (e.g., sleep(60)) to mimic natural user behavior and avoid rate-limiting issues.
	•	Comment Text: Comments are dynamically generated based on tweet content to ensure relevance and authenticity.
	•	Bookmark and Retweet: These actions are only taken on highly relevant tweets to maximize engagement.

This documentation provides a detailed guide to using and understanding the functionality of each endpoint and feature within the Twitter Engagement Bot. Please feel free to reach out if there are further questions or specific requirements for engagement criteria.