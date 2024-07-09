def filter_lines(keyword):
    print(f"Looking for {keyword}")
    try:
        while True:  # Нескінченний цикл, де генератор чекає на вхідні дані
            line = yield  # Отримання рядка через send()
            if keyword in line:  # Перевірка на наявність ключового слова
                yield f"Line accepted: {line}"
            else:
                yield None
    except GeneratorExit:
        print("Generator closed")

if __name__ == "__main__":
    # Створення і старт генератора
    gen = filter_lines("hello")
    next(gen)  # Потрібно для старту генератора
    messages = ["this is a test", "hello world", "another hello world line", "hello again", "goodbye"]
    hello_messages = []
    # Відправлення даних у генератор
    for message in messages:
        result = gen.send(message)  # Відправляємо повідомлення в генератор
        if result:  # Додаємо результат тільки якщо він не None
            hello_messages.append(result)
        next(gen)  # Продовжуємо до наступного yield: інструкція line = yield

    # Закриття генератора
    gen.close()
    print(hello_messages)


