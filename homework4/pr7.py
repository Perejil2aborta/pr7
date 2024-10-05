a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
c = float(input("Введите значение c: "))


if b != 0:
    x = a / b + c * a
    print(f"Результат: {x}")
else:
    print("Ошибка:деление на ноль невозможно")
