#!/usr/bin/env python3
"""
Простой Chatbot для новичков
Пример как писать простой интерактивный чат-бот
"""


def get_response(user_input):
    """
    Получить ответ бота на вход пользователя

    Args:
        user_input (str): То что написал пользователь

    Returns:
        str: Ответ бота
    """
    # Приводим текст к нижнему регистру для сравнения
    user_input = user_input.lower().strip()

    # Словарь с ответами
    responses = {
        "привет": "Привет! 👋 Как дела?",
        "hi": "Hello! 👋",
        "как дела": "У меня все хорошо! 😊 А у тебя?",
        "how are you": "I'm doing great! 😊",
        "что ты умеешь": "Я простой chatbot! Могу отвечать на вопросы. Спроси меня что угодно!",
        "who are you": "I'm a simple chatbot! Nice to meet you!",
        "пока": "До встречи! 👋 Приходи еще!",
        "bye": "Goodbye! 👋",
        "exit": "Выход...",
        "quit": "Выход...",
    }

    # Если нашли точное совпадение
    if user_input in responses:
        return responses[user_input]

    # Если нашли слово в ответах
    for key, value in responses.items():
        if key in user_input:
            return value

    # Если не нашли - ответить по умолчанию
    return "Интересно! 🤔 Не совсем тебя понял. Попробуй спросить что-то другое!"


def main():
    """Главная функция программы"""
    print("=" * 50)
    print("🤖 Добро пожаловать в Simple Chatbot! 🤖")
    print("=" * 50)
    print("Введи 'пока' или 'exit' чтобы выйти\n")

    while True:
        # Получаем ввод от пользователя
        user_input = input("Ты: ").strip()

        # Если пусто - пропускаем
        if not user_input:
            continue

        # Получаем ответ
        response = get_response(user_input)
        print(f"Chatbot: {response}\n")

        # Выход
        if user_input.lower() in ["пока", "bye", "exit", "quit"]:
            break

    print("\nСпасибо что общался со мной! До встречи! 👋")


if __name__ == "__main__":
    main()
