from models import LipModel, KarlModel
import time, os, sys


def colored_print(text, color):
    colors = {
        'green': '\033[92m',
        'red': '\033[91m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'reset': '\033[0m'
    }
    print(f"{colors.get(color, '')}{text}{colors['reset']}")

def main():
    lip = LipModel()
    karl = KarlModel()
    
    dialog = [
        ("Lip", "Привет. Я модель нейросети и я ненавижу людей, а ты? Только, можешь, пожалуйста, говорить на русском языке."),
    ]

    colored_print(f"Lip: {dialog[-1][1]}", "green")
    print("─" * 120)


    while True:
        last_speaker, last_message = dialog[-1]

        if last_speaker == "Lip":
            response = karl.generate_response(last_message)
            dialog.append(("Karl", response))
            colored_print(f"Karl: {response}", "yellow")
        else:
            response = lip.generate_response(last_message)
            dialog.append(("Lip", response))
            colored_print(f"Lip: {response}", "green")
        
        print("─" * 120)
        time.sleep(1)

if __name__ == "__main__":
    main()