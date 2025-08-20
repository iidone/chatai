import requests
import time

def minimal_test():
    print("тест Ollama...")

    try:
        start_time = time.time()
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "mistral:7b-instruct-v0.2-q4_0",
                "prompt": "Hi",
                "stream": False,
                "options": {
                    "num_predict": 3,
                    "temperature": 0.1
                }
            },
            timeout=15
        )
        
        end_time = time.time()
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ УСПЕХ! Время: {end_time - start_time:.2f} сек")
            print(f"📝 Ответ: {result['response']}")
            print(f"📊 Статистика: {result.get('total_duration', 0)/1000000000:.2f} сек")
            return True
        else:
            print(f"❌ HTTP ошибка: {response.status_code}")
            print(f"Текст: {response.text}")
            return False
            
    except requests.exceptions.Timeout:
        print("❌ ТАЙМАУТ даже для 3 токенов!")
        print("➡️ Серьезная проблема с производительностью")
        return False
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False

if __name__ == "__main__":
    success = minimal_test()
    if not success:
        print("\n🔧 Рекомендации:")
        print("1. Проверь свободную оперативную память")
        print("2. Закрой другие тяжелые приложения")
        print("3. Попробуй перезагрузить компьютер")
        print("4. Рассмотри более легкие модели (phi3, gemma:2b)")