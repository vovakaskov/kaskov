try:
    N = int(input("Введите количество чисел N: "))
    if N <= 0:
        print("Количество чисел должно быть больше 0.")
        exit()
except ValueError:
    print("Ошибка: N должно быть целым числом.")
    exit()

print(f"Введите {N} чисел через пробел:")
numbers = list(map(int, input().split()))

if len(numbers) != N:
    print(f"Ошибка: вы ввели {len(numbers)} чисел, а требовалось {N}.")
    exit()

count = 0
total_sum = 0

for num in numbers:
    if num % 5 == 0 and num % 10 != 0:
        count += 1
        total_sum += num

print(f"Количество подходящих элементов: {count}")
print(f"Сумма подходящих элементов: {total_sum}")