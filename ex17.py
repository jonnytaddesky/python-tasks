a = int(input())
b = int(input())

if b != 0:
    print(a / b)
else:
    print('Деление невозможно')
    b = int(input('Введите корректное число b: '))
    if b == 0:
        print('Пользователь не справился')
    else:
        print(a / b)