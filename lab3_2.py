import math
a = 0.1
b = 1.5
step = 0.05
print("Таблица значений функции y:")
print("-" * 30)
print(f"{'x':>8} | {'y':>15}")
print("-" * 30)
x = a
while x <= b + 1e-9: 
    try:
        term1 = x ** (1 / (2 * x))
        denominator = math.sin(x)**2 + math.cos(x)**2
        term2 = (x**2 * math.log(x**3)) / denominator
        y = term1 + term2
        print(f"{x:8.2f} | {y:15.6f}")
    except ValueError as e:
        print(f"{x:8.2f} | Ошибка: {e}")
    x += step

print("-" * 30)