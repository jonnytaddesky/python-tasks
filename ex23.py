x = float(input())
y = float(input())
operation = input()

if operation == '+':
    print(x + y)
elif operation == '-':
    print(x - y)
elif operation == '*':
    print(x * y)
elif operation == 'pow':
    print(x ** y)
elif operation == 'mod':
    if y == 0:
        print('Деление на 0!')
    else:
        print(x % y)
elif operation == '/':
    if y != 0:
        print(x / y)
    else:
        print('Деление на 0!')
elif operation == 'div':
    if y != 0:
        print(x // y)
    else:
        print('Деление на 0!')

