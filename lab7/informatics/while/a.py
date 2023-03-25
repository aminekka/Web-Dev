# Входные данные
# Задано единственное целое число N

# Выходные данные
# Необходимо вывести  все точные квадраты натуральных чисел, не превосходящие данного числа N.

import math
a = int(input())
i = 1
# b = int(input())

while i<=a:
    if(math.sqrt(i) == int(math.sqrt(i))):
        print(i, end='\n')
    i+=1



# for i in range(a, b+1):
#     if(math.sqrt(i) == int(math.sqrt(i))):
#         print(i, end=' ')