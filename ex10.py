X = int(input())
H = int(input())
M = int(input())

minutes = H * 60 + M + X

print(minutes // 60)
print(minutes % 60)

