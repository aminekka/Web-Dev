n = input()
num=0

for i in range(len(n)):
        d = int(n[i])
        num+=d*(2**(len(n)-i-1))

print(num)

