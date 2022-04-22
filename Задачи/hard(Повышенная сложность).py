# 8. Даны два целых числа a и b. Если a делится на b или b делится на a, то вывести 1, иначе –
# любое другое число. Условные
# операторы и операторы цикла не использовать.

import random
a = int(input("Print a -"))
b = int(input("Print b - "))
if a % b == 0 or b % a == 0:
    print(1)
else:
    print(random.randint(-100, 100))