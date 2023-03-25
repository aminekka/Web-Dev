x = int(input())
b=''

while x%10==0:
    x//=10


for i in str(x):
    b = i + b

print(b)


