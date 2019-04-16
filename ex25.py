a = int(input()) 
b = int(input())
c = int(input())

if a > b and a > c:
    max = a
    if b > c:
        mid = b
        min = c
    else:
        mid = c
        min = b
    print(max)
    print(min)
    print(mid)
elif b > a and b > c:
    max = b
    if a > c:
        mid = a
        min = c
    else:
        mid = c
        min = a
    print(max)
    print(min)
    print(mid)
elif c > a and c > b:
    max = c
    if a > b:
        mid = a
        min = b
    else:
        mid = b
        min = a
    print(max)
    print(min)
    print(mid)
elif a == c and b == c:
    max = a
    min = b
    mid = c
    print(max)
    print(min)
    print(mid)
elif a == b and (c < a or c < b):
    max = a
    min = c
    mid = b
    print(max)
    print(min)
    print(mid)
elif a == b and (c > a or c > b):
    max = c
    min = a
    mid = b
    print(max)
    print(min)
    print(mid)
elif a == c and (b < a or b < c):
    max = a
    min = b
    mid = c
    print(max)
    print(min)
    print(mid)
elif a == c and (b > a or b > c):
    max = b
    min = a
    mid = c
    print(max)
    print(min)
    print(mid)
elif b == c and (a < b or a < c):
    max = b
    min = a
    mid = c
    print(max)
    print(min)
    print(mid)
elif b == c and (a > b or a > c):
    max = a
    min = b
    mid = c
