figure = input()

if figure == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())

    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5

    print(s)
elif figure == 'прямоугольник':
    a = int(input())
    b = int(input())

    s = a * b
    print(s)
elif figure == 'круг':
    radius = int(input())
    s = 3.14 * radius ** 2
    print(s)