def find_min(a, b, c, d):
    min = a
    
    if b < min:
        min = b
    if c < min:
        min = c
    if d < min:
        min = d
        
    print(min)

a, b, c, d = map(int, input().split())
find_min(a, b, c, d)
