using System;

namespace IndividualTask
{
    /// <summary>
    /// Класс для хранения массива вещественных чисел и методов работы с ним.
    /// </summary>
    public class ArrayProcessor
    {
        // Внутренний массив вещественных чисел
        private double[] _data;

        /// <summary>
        /// Количество элементов в массиве.
        /// </summary>
        public int Length => _data?.Length ?? 0;

        /// <summary>
        /// Конструктор: создаёт массив заданного размера.
        /// </summary>
        /// <param name="size">Количество элементов (N).</param>
        public ArrayProcessor(int size)
        {
            if (size <= 0)
                throw new ArgumentException("Размер массива должен быть положительным.");

            _data = new double[size];
        }

        /// <summary>
        /// Индексатор для доступа к элементам массива.
        /// </summary>
        public double this[int index]
        {
            get => _data[index];
            set => _data[index] = value;
        }

        /// <summary>
        /// Заполняет массив значениями, введёнными с клавиатуры.
        /// </summary>
        public void ReadFromConsole()
        {
            for (int i = 0; i < _data.Length; i++)
            {
                Console.Write($"Введите элемент [{i}]: ");
                while (!double.TryParse(Console.ReadLine(), out _data[i]))
                {
                    Console.Write("Некорректный ввод. Повторите: ");
                }
            }
        }

        /// <summary>
        /// Проверяет утверждение:
        /// "Никакой положительный элемент не превосходит по модулю
        ///  любой отрицательный элемент, расположенный правее него."
        /// </summary>
        /// <returns>true — утверждение верно; false — найдено нарушение.</returns>
        public bool CheckCondition()
        {
            // Перебираем все положительные элементы
            for (int i = 0; i < _data.Length; i++)
            {
                if (_data[i] <= 0) continue; // нас интересуют только положительные

                // Ищем отрицательные элементы правее i
                for (int j = i + 1; j < _data.Length; j++)
                {
                    if (_data[j] >= 0) continue; // нас интересуют только отрицательные

                    // Если положительный элемент по модулю больше |отрицательного| — нарушение
                    if (_data[i] > Math.Abs(_data[j]))
                        return false;
                }
            }

            return true;
        }

        /// <summary>
        /// Выводит массив в консоль в удобном виде.
        /// </summary>
        public void Print()
        {
            Console.WriteLine("Массив: [" + string.Join("; ", _data) + "]");
        }
    }
}
