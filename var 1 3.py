x = float(input("Введите координату x: "))
a = float(input("Введите начало отрезка a: "))
b = float(input("Введите конец отрезка b: "))

if min(a, b) <= x <= max(a, b):
    print(f"Точка x = {x} попадает в отрезок [{a}, {b}]")
else:
    print(f"Точка x = {x} НЕ попадает в отрезок [{a}, {b}]")