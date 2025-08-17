import requests
import json

class LlamaModel:
    def generate_response(self, prompt: str) -> str:
        url = "http://localhost:11434/api/generate"
        payload = {
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
        response = requests.post(url, json=payload)
        return json.loads(response.text)["response"]

class MistralModel:
    def generate_response(self, prompt: str) -> str:
        url = "http://localhost:11434/api/generate"
        payload = {
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }
        response = requests.post(url, json=payload)
        return json.loads(response.text)["response"]