"""

В римской системе счисления для обозначения чисел используются следующие символы (справа записаны числа, которым они соответствуют в десятичной системе счисления):

I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000
Будем использовать вариант, в котором числа 4, 9, 40, 90, 400 и 900 записываются как вычитание из большего числа меньшего: IV, IX, XL, XC, CD и CM, соответственно.

Формат ввода:
Строка, содержащая натуральное число n, 0<n<4000.

Формат вывода:
Строка, содержащая число, закодированное в римской системе счисления.

Sample Input 1:

1984
Sample Output 1:

MCMLXXXIV
Sample Input 2:

9
Sample Output 2:

IX
Sample Input 3:

3
Sample Output 3:

III
"""

def int2roman(number):
    numerals = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
                50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    result = ""
    for value, numeral in numerals.items():  # in Python 3.6 dict keep order
        while number >= value:
            result += numeral
            number -= value
    return result


def main():
    number = int(input())
    print(int2roman(number))


if __name__ == '__main__':
    main()
