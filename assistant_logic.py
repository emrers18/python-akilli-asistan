import random

def fake_smart_assistant(user_message:str) -> str:

    responses = [
        "Merhaba, size nasıl yardımcı olabilirim?",
        "Tabii, bu konuda size destek olmaya çalışayım.",
        "Anladım, isterseniz bunu birlikte inceleyebiliriz.",
        "Elbette, size yardımcı olmak için buradayım."
    ]

    return random.choice(responses)


if __name__ == "__main__":
    user_text = input("Bir mesaj yazın: ")
    answer = fake_smart_assistant(user_text)
    print(f"Asistan Cevabı: {answer}")

