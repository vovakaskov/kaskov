def find_elements_greater_than_neighbors_sum(matrix):
    """
    Находит все элементы матрицы, которые превосходят сумму своих соседей.
    Соседи - элементы, у которых ровно один индекс отличается на 1.
    """
    if not matrix or not matrix[0]:
        return []
    
    n = len(matrix)
    m = len(matrix[0])
    result = []
    
    for i in range(n):
        for j in range(m):
            # Собираем соседей: ровно один индекс отличается на 1
            neighbors = []
            
            # Соседи по строке (i±1, j)
            if i - 1 >= 0:
                neighbors.append(matrix[i-1][j])
            if i + 1 < n:
                neighbors.append(matrix[i+1][j])
            
            # Соседи по столбцу (i, j±1)
            if j - 1 >= 0:
                neighbors.append(matrix[i][j-1])
            if j + 1 < m:
                neighbors.append(matrix[i][j+1])
            
            # Проверяем условие
            if matrix[i][j] > sum(neighbors):
                result.append((i, j, matrix[i][j], sum(neighbors)))
    
    return result


def main():
    # Пример ввода: размерность и элементы матрицы
    print("Введите количество строк и столбцов:")
    n, m = map(int, input().split())
    
    print("Введите элементы матрицы построчно:")
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    
    result = find_elements_greater_than_neighbors_sum(matrix)
    
    print("\nЭлементы, превосходящие сумму своих соседей:")
    print("Индекс (i, j) | Значение | Сумма соседей")
    print("-" * 45)
    
    if not result:
        print("Таких элементов нет.")
    else:
        for i, j, value, neighbors_sum in result:
            print(f"({i}, {j})       | {value:^8} | {neighbors_sum}")


if __name__ == "__main__":
    main()
