import random
import openai
import requests
import json


def get_gpt4_response(prompt = "Generate a spooky fact:", api_key = "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"):
    endpoint_url = "https://api.openai.com/v1/engines/text-curie-001/completions"  # 'davinci' is a typical GPT-4 engine, but you might want to confirm the exact endpoint from OpenAI documentation.
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "User-Agent": "OpenAI-Python"
    }
    
    data = {
        "prompt": prompt,
        "max_tokens": 150  # You can adjust max_tokens as needed.
    }
    
    response = requests.post(endpoint_url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        response_json = response.json()
        return response_json["choices"][0]["text"].strip()
    else:
        raise Exception(f"API call failed with status code {response.status_code}: {response.text}")

words = ['apple', 'banana', 'cherry', 'date', 'elderberry']

def get_random_word():
    return random.choice(words)
    
import openai

# Set up your OpenAI API key
api_key = "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"
openai.api_key = api_key

def generate_spooky_fact():
    prompt = "Tell me a spooky fact:"
    response = openai.Completion.create(
        engine="davinci",  # You can choose a different engine if needed
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None
    )
    return response
    return response.choices[0].text.strip()

# Example usage
if __name__ == "__main__":
    api_key = "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"

    prompt = "Here is a spooky Halloween themed fact:"
    spooky_fact = get_gpt4_response(api_key=api_key, prompt=prompt)
    print(str(spooky_fact))
