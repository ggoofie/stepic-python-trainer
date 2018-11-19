"""

Последовательность n>0 целых чисел называется jolly jumper в случае, если значения абсолютных разностей последовательных элементов принимают все возможные значения между 1 и n−1.

Например, последовательность 1 -3 -4 -1 1 является jolly jumper последовательностью, так как абсолютные разности равны 4 1 3 2, соответственно, а n−1=4.
Будем считать, что последовательность из одного числа является jolly jumper.

Напишите программу, которая проверяет, является ли введённая последовательность jolly jumper.

Формат ввода:

Строка, содержащая 1≤n≤10000 целых чисел, разделённых пробелом.

Формат вывода:
Одна строка, содержащая "Jolly" (без кавычек), если последовательность является jolly jumper и "Not jolly" в противном случае.

Sample Input 1:

1 -3 -4 -1 1
Sample Output 1:

Jolly
Sample Input 2:

1 3 5
Sample Output 2:

Not jolly
Sample Input 3:

4
Sample Output 3:

Jolly
"""

import sys


def jolly(lst):
    n = len(lst)
    res = {abs(lst[i] - lst[i + 1]) for i in range(0, n - 1)}
    if res == set(range(1, n)):
        return 'Jolly'
    return 'Not jolly'


def main():
    reader = (map(int, line.split()) for line in sys.stdin)
    lst = list(*reader)
    print(jolly(lst))


if __name__ == '__main__':
    main()
