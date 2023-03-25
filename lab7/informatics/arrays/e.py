# Дан массив, состоящий из целых чисел. Напишите программу, которая определяет, есть ли в массиве пара соседних элементов с одинаковыми знаками.

n = int(input())
a = list(map(int, input().split()))
cnt=0

for i in range(1, len(a)):
    if a[i-1]>0 and a[i]>0 or a[i-1]<0 and a[i]<0:
        cnt+=1

if cnt>0:
    print('YES')
else:
    print('NO')        