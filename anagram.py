"""

Напишите программу, которая проверяет, являются ли два введённых слова анаграммами.

Программа должна вывести True в случае, если введённые слова являются анаграммами, и False в остальных случаях.

Формат ввода:

Два слова, каждое на отдельной строке. 
Слово может состоять только из латинских символов произвольного регистра. Регистр символов не должен влиять на ответ.

Формат вывода:
True или False.

Sample Input 1:

silent
listen
Sample Output 1:

True
Sample Input 2:

AbaCa
AcaBa
Sample Output 2:

True
Sample Input 3:

abaca
acada
Sample Output 3:

False
"""

from collections import Counter


def isAnagram(s1, s2):
    if Counter(s1.lower()) == Counter(s2.lower()):
        return 'True'
    return 'False'  


s1, s2 = input(), input()
print(isAnagram(s1, s2))
