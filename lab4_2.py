import math
P = 1.0
for n in range(1, 16):
    numerator = (n**4) / 4 + (n**3) / 3 + (n**2) / 2 + n
    denominator = 3 * (n**3) + 2 * (n**2) + n
    term = (numerator / denominator) * math.log(n + 1)
    P *= term

print(f"Произведение P = {P:.6f}")