from models import LlamaModel, MistralModel
import time

def main():
    llama = LlamaModel()
    mistral = MistralModel()
    
    dialog = [
        ("Llama3", "Привет!"),
    ]
    
    print(f"Llama3: {dialog[-1][1]}")

    for i in range(5):
        last_speaker, last_message = dialog[-1]

        if last_speaker == "Llama3":
            response = mistral.generate_response(last_message)
            dialog.append(("Mistral", response))
            print(f"Mistral: {response}")
        else:
            response = llama.generate_response(last_message)
            dialog.append(("Llama3", response))
            print(f"Llama3: {response}")
        
        time.sleep(3)

if __name__ == "__main__":
    main()