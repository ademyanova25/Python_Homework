# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def func(a, b, c):
    if a == b == c:
        return a
    elif a > b > c:
        return a
    elif b > a > c:
        return b
    else:
        return c


print(func(int(input('Введите первую переменную: ')),
           int(input('Введите вторую переменную: ')),
           int(input('Введите третью переменную: '))))
