"""

Выведите таблицу размером n×n, заполненную целыми числами от 1 до n2 по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере.

Формат ввода:
Одна строка, содержащая одно целое число n, n>0.

Формат вывода:
Таблица из n строк, значения в строках разделены пробелом.

Sample Input:

5
Sample Output:

1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
"""

def spiral(n):
    dx, dy = 1, 0  # Starting increments
    x, y = 0, 0  # Starting location
    l = [[None] * n for j in range(n)]
    for i in range(1, n ** 2 + 1):
        l[x][y] = i
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and l[nx][ny] is None:
            x, y = nx, ny
        else:
            dx, dy = -dy, dx
            x, y = x + dx, y + dy
    return l


def printspiral(l):
    n = range(len(l))
    for y in n:
        for x in n:
            print("%2i" % l[x][y], end=' ')
        print()


def main():
    n = int(input())
    printspiral(spiral(n))


if __name__ == "__main__":
    main()
