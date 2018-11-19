"""

Напишите программу, вычисляющую следующее состояние поля для Game of life. 

Поле представляет собой прямоугольник, причём для крайних клеток поля соседними являются клетки с противоположного конца (поле представляет собой тор).

Формат ввода:

На первой строке указаны два целых числа через пробел -- высота и ширина поля. 
В следующих строках подаётся состояние поля. Точка "." обозначает мёртвую клетку, символ "X" − живую. 

Формат вывода:
Следующее состояние поля, используя те же обозначения, что использовались на вводе.

Sample Input 1:

5 5
.....
..X..
...X.
.XXX.
.....
Sample Output 1:

.....
.....
.X.X.
..XX.
..X..
Sample Input 2:

5 5
.....
.....
.XXX.
.....
.....
Sample Output 2:

.....
..X..
..X..
..X..
.....
Sample Input 3:

5 6
...XX.
.XX...
..X...
XX....
X..XX.
Sample Output 3:

.X..XX
.XX...
X.X...
XXXX.X
XXXXX.
"""

import sys
import copy


def life(n, m, a):
    result = copy.deepcopy(a)
    foo = lambda y, x: x - 1 if y < 0 else (0 if y >= x else y)
    for i in range(n):
        for j in range(m):
            count_alive = 0
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    if di == dj == 0:
                        continue
                    ai = foo(i + di, n)
                    aj = foo(j + dj, m)
                    if a[ai][aj] == 'X':
                        count_alive += 1
            if a[i][j] == '.' and count_alive == 3:
                result[i][j] = 'X'
            elif a[i][j] == 'X' and (count_alive not in (2, 3)):
                result[i][j] = '.'
    return result


def main():
    reader = (line for line in sys.stdin)
    n, m = map(int, next(reader).split())
    field = [list(line.strip()) for line in reader]
    for line in life(n, m, field):
        print(''.join(line))


if __name__ == '__main__':
    main()
    
