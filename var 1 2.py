a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

if a > b:
    print(f"Большее число: {a}")
elif b > a:
    print(f"Большее число: {b}")
else:
    print("Числа равны")