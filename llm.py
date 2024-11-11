from ollama import get_ollama_response
from prompts import get_is_tweet_beneficial_prompt, get_is_tech_job_tweet_beneficial_prompt


def is_tweet_beneficial(tweet_text):
    prompt = get_is_tweet_beneficial_prompt(tweet_text)
    return get_ollama_response(prompt)

def is_tech_job_tweet_beneficial(tweet_text):
    prompt = get_is_tech_job_tweet_beneficial_prompt(tweet_text)
    return get_ollama_response(prompt)
