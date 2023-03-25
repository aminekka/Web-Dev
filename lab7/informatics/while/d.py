# Дано натуральное число N. Выведите слово YES, если число N является точной степенью двойки, или слово NO в противном случае.
# import math
# n = int(input())
# i = 0

# if n==1:
#     print('YES')
# else:
#     while n>1:
#         if n%2==0:
#             n = n/2
#         else:
#             print('NO')
#             break


# while 2**i<=n:
#     if(n == 2**i):
        
#     else:
#         print('NO')
#     i+=1











# n = int(input("Enter a natural number: "))

# if n == 1:
#     print("YES")
# else:
#     while n > 1:
#         if n % 2 == 0:
#             n = n / 2
#         else:
#             print("NO")
#             break
#     else:
#         print("YES")








n = int(input())

pow = 1

while pow < n:
    pow *= 2

if pow == n:
    print("YES")
else:
    print("NO")


