tickets = str(input())
x1 = tickets[0]
x2 = tickets[1]
x3 = tickets[2]
x4 = tickets[3]
x5 = tickets[4]
x6 = tickets[5]

sum1 = int(x1) + int(x2) + int(x3)
sum2 = int(x4) + int(x5) + int(x6)

if sum1 == sum2:
    print('Счастливый')
else:
    print('Обычный')

