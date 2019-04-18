x = int(input())

if x % 10 == 1 and x % 100 != 11:
    print(str(x), 'программист')
elif 11 <= x <= 20 or x % 10 == 0 or x % 10 == 5 \
    or x % 10 == 6 or x % 10 == 7 or x % 10 == 8 or x % 10 == 9:
    print(str(x), 'программистов')
elif x % 100 == 11 or x % 100 == 12 or x % 100 == 13 \
    or x % 100 == 14 or x % 100 == 15 or x % 100 == 16 or x % 100 == 17 \
        or x % 100 == 18 or x % 100 == 19 or x % 100 == 20:
    print(str(x), 'программистов')
elif (x % 10 == 2 or x % 10 == 3 or x % 10 == 4) and x != 12 and x != 13 and x != 14:
    print(str(x), 'программиста')

