import math
S = 0
for n in range(1, 51):
    numerator = 2.2 ** (2 * n + 1)    
    denominator = math.factorial(2 * n + 1) 
    S += numerator / denominator         
print(f"Сумма ряда S = {S:.6f}")