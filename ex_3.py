def square_numbers():
    try:
        while True:  # Безкінечний цикл для прийому чисел
            number = yield  # Отримання числа через send()
            square = number ** 2  # Піднесення до квадрата
            yield square  # Повернення результату
    except GeneratorExit:
        print("Generator closed")

# Створення і старт генератора
gen = square_numbers()

while True:
    user_input=input(">>>")
    # Ініціалізація генератора
    next(gen)  # Або gen.send(None), щоб стартувати

    # Відправлення числа в генератор і отримання результату
    if not user_input:
        gen.close()
        break
    result = gen.send(int(user_input))  # Повинно повернути число
    print(f"Square of {user_input}: {result}")
