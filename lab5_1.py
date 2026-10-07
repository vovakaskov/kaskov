try:
    N = int(input("Введите количество целых чисел N: "))
    if N <= 0:
        print("Количество чисел должно быть больше 0.")
        exit()
except ValueError:
    print("Ошибка: N должно быть целым числом.")
    exit()

print(f"Введите {N} целых чисел через пробел:")
numbers = list(map(int, input().split()))

if len(numbers) != N:
    print(f"Ошибка: вы ввели {len(numbers)} чисел, а требовалось {N}.")
    exit()

first_abs = abs(numbers[0])

count = 0
for num in numbers:
    if abs(num) == first_abs:
        count += 1

print(f"Количество элементов, совпадающих по модулю с первым ({numbers[0]}): {count}")