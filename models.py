import requests
import json

class LlamaModel:
    def generate_response(self, prompt: str) -> str:
        url = "http://localhost:11434/api/generate"
        payload = {
            "model": "llama3:8b-instruct-q4_0",
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.7,
                "top_p": 0.9
            }
        }
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            result = response.json()
            return result["response"][:1000]
        except Exception as e:
            print(f"Ошибка Llama3: {e}")
            return "Извините, произошла ошибка."

class MistralModel:
    def generate_response(self, prompt: str) -> str:
        url = "http://localhost:11434/api/generate"
        payload = {
            "model": "mistral:7b-instruct-v0.2-q4_0", 
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.7,
                "top_p": 0.9
            }
        }
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            result = response.json()
            return result["response"][:1000]
        except Exception as e:
            print(f"Ошибка Mistral: {e}")
            return "Извините, произошла ошибка."