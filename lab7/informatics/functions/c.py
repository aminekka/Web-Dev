def xor(a, b):
    if a!=b:
        print(1)
    else:
        print(0)

a, b = map(int, input().split())
xor(a,b)