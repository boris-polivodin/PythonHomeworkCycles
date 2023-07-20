# Задача 12: 
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# x + y = s
# x * y = p = x * (s - x) = -x*x + s*x

import random
import math

firstNumber  = random.randint(1, 1000)
secondNumber = random.randint(1, 1000)

sum = firstNumber + secondNumber;
mult = firstNumber * secondNumber;

# решаем квадратное уравнение x*x - s*x + p = 0
dis = sum*sum - 4*mult
firstNumberCalc = -(math.sqrt(dis) - sum)/2 # оставляем только потенциально положительный корень
secondNumberCalk = sum - firstNumberCalc
print(f"Петя задумал {firstNumber} и {secondNumber}. Их сумма = {sum}, а произведение = {mult} ")
print(f"Катя отгадала {int(firstNumberCalc)} и {int(secondNumberCalk)}")
