def my_generator():
    try:
        yield "Working"
    except GeneratorExit:
        print("Generator is being closed")

gen = my_generator()
print(next(gen))  # Отримуємо "Working"
gen.close()  # Викликаємо закриття генератора
