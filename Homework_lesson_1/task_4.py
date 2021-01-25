a = int(input('Введите число: '))
b = a % 10
c = a // 10
while c > 0:
    if c % 10 > b:
        b = c % 10
    c = c // 10
print(b)
