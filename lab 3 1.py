import math
x = 1.5
y = math.exp(2 * x) * math.log(2 + x) - (2 ** (2 * x)) * math.log(2 - x)
print(f"{y:.5f}")