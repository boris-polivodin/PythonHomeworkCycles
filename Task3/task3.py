# Задача 14: 
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

import math

number = int(input("Задайте число N: "))
if number >= 2:
    temp = 2
    counter = 1
    while temp <= number:
        print(temp)
        counter += 1
        temp = int(math.pow(2, counter))