"""

Напишите программу, которая принимает на вход матрицу, выполняет её транспонирование и выводит результат.

Формат ввода:
В первой строке указываются два целых числа n и m, количество строк и столбцов, соответственно.
Далее следуют n строк, содержащих по m целых чисел, разделённых пробелом.

Формат вывода:
Программа должна вывести m строк содержимого транспонированной матрицы. Элементы матрицы стоит разделять пробелом.

Sample Input 1:

2 3
1 2 3
4 5 6
Sample Output 1:

1 4
2 5
3 6
Sample Input 2:

2 2
1 2
3 4
Sample Output 2:

1 3
2 4
"""

import sys


def matrix_transpose(matrix):
    return [list(i) for i in zip(*matrix)]


def main():
    reader = (list(map(int, line.split())) for line in sys.stdin)
    n, m = next(reader)
    matrix = list(reader)
    for line in matrix_transpose(matrix):
        print(*line, sep=' ')


if __name__ == '__main__':
    main()
    
