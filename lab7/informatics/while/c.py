# По данному числу N распечатайте все целые степени двойки, не превосходящие N, в порядке возрастания

n = int(input())
i=0

while 2**i<=n:
    print(2**i, end=' ')
    i+=1
    