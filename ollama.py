import json
import os

import requests

url = os.getenv("LLM_URL")

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': os.getenv("LLM_API_KEY")
}


def get_ollama_response(prompt):
    payload = json.dumps({
        "prompt": prompt
    })
    response = requests.request("POST", url, headers=headers, data=payload)
    return json.loads(response.json()["response"])
