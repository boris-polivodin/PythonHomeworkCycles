# Задача 10: 
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

import random

countCoin = int(input("Задайте число монеток: "))
countTails = 0
countHeads = 0
for i in range(1, countCoin + 1):
    temp = random.randint(0,1)
    print(temp)
    if temp == 0:
        countTails += 1
    else:
        countHeads += 1
if countTails < countHeads:
    print(f"Нужно перевернуть {countTails} решки")
elif countHeads < countTails:
    print(f"Нужно перевернуть {countHeads} орла")
else:
    print(f"Количество орлов {countHeads} и решек {countTails} одинаковое")