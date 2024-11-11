import json
import os

import google.generativeai as genai
from flask import jsonify

from ollama import get_ollama_response

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model_name = "gemini-1.5-flash"
generation_config = genai.GenerationConfig(
    temperature=1,
    top_p=0.95,
    top_k=64,
    max_output_tokens=8192,
    response_mime_type="application/json"
)

model = genai.GenerativeModel(model_name, generation_config=generation_config)


def get_gemini_response(prompt):
    try:
        response = model.generate_content(prompt)
        json_res = jsonify(response.text)
        return json.loads(json_res.json)
    except Exception as e:
        print(f"Error occurred: {e}")
        return get_ollama_response(prompt)
