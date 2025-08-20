import requests
import json
import re

def truncate_complete_sentences(text: str, max_length: int = 1000) -> str:
    if len(text) <= max_length:
        return text
    
    truncated = text[:max_length]

    match = re.search(r'[.!?]\s+[А-ЯA-Z]', truncated[::-1])
    if match:
        end_pos = max_length - match.start()
        return truncated[:end_pos]

    last_space = truncated.rfind(' ')
    if last_space > 0:
        return truncated[:last_space]
    
    return truncated

class LipModel:
    def generate_response(self, prompt: str) -> str:
        url = "http://localhost:11434/api/generate"
        payload = {
            "model": "llama3:8b-instruct-q4_0",
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.7,
                "top_p": 0.9,
                "num_predict": 500
            }
        }
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            result = response.json()
            return truncate_complete_sentences(result["response"])
        except Exception as e:
            print(f"Ошибка Lip: {e}")
            return "Извините, произошла ошибка."

class KarlModel:
    def generate_response(self, prompt: str) -> str:
        url = "http://localhost:11434/api/generate"
        payload = {
            "model": "llama3:8b-instruct-q4_0", 
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.7,
                "top_p": 0.9,
                "num_predict": 500
            }
        }
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            result = response.json()
            return truncate_complete_sentences(result["response"])
        except Exception as e:
            print(f"Ошибка Karl: {e}")
            return "Извините, произошла ошибка."