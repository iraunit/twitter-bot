
def get_is_tweet_beneficial_prompt(text):
    return f"""
    Analyze the following tweet data to determine if engaging with it would be beneficial for increasing engagement with a tech-focused account. The account aims to attract users interested in job listings, coding contests, tech blogs, and software development resources. 

Consider the following questions:
1. Does this tweet mention coding, tech jobs, contests, or software development topics?
2. Would liking this tweet or commenting on it help promote tech resources and engage with a community interested in tech?
3. Is this tweet likely to be shared on social media or in a tech community so that they learn something instead of wasting time?
4. Tweet should not me spammy or just for the sake of engagement and getting likes and followers.
5. Like the tweet if I am engaging with the tweet like retweeting/commenting/bookmarking/liking
6. Make sure the tweet contain only english language else don't engage

Based on this analysis, return a JSON response with the following structure:

{{
  "beneficial_for_engagement": true/false,  // Whether engaging is beneficial
  "like_tweet": true/false,                 // Whether to like the tweet
  "comment_on_tweet": true/false,           // Whether to comment on the tweet ( I only want to comment on the best tweets possible related to coding and tech )
  "comment_text": string/null               // If commenting, provide a suggested comment, ( less than 250 characters including spaces as well)
}}

Tweet Data is below:

{text}
"""


def get_is_tech_job_tweet_beneficial_prompt(text):
    return f"""
    Analyze the following tweet to determine if it relates to a genuine, high-paying tech job posting suitable for freshers or candidates with less than 1 year of experience. The focus is on roles like software development (SDE), DevOps, backend/frontend development, or software engineering internships, especially in top product-based companies or startups.

Consider the following questions to filter out unrelated tweets:
1. Does the tweet specifically mention a tech-related position (e.g., SDE, DevOps, software engineering internship, backend/frontend developer)?
2. Is the job aimed at freshers or individuals with less than 2 year of experience if its mentioned?
3. Is the job offer from a reputable source, suggesting a high-paying role in a top company or startup?
4. Confirm that the tweet does not seem spammy or solely aimed at boosting likes or followers.
5. Also I am not looking for job but this is for my followers
6. Verify that the job mentioned in the tweet required less than 2 years of experience if experience is mentioned or is for SDE 1 or SDE - I
7. The job should be for India only or remote job
8. Like the tweet if I am engaging with the tweet like retweeting/commenting/bookmarking/liking
9. Make sure the tweet contain only english language else don't engage

Confirm at least twice that the tweet is indeed related to a genuine tech job to ensure accuracy.

Based on this analysis, return a JSON response with the following structure:

{{
  "beneficial_for_engagement": true/false,  // Whether engaging is beneficial
  "like_tweet": true/false,                 // Whether to like the tweet
  "retweet_tweet": true/false               // Whether to retweet for my followers to apply for jobs ( I am not looking for job but this is for my followers )
  "bookmark_tweet": true/false              // Whether to bookmark the tweet
  "emails": string/null                     // parse the emails from the tweet of the recruiter
}}

Tweet Data is below:

{text}
"""