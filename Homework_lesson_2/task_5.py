lst = [7, 5, 3, 3, 2]
a = int(input('Введите рейтинг: '))

for i in lst:
    if a in lst:
        b = lst.index(a)
        c = lst.count(a)
        d = b * c
        lst.insert(d, a)
    else:
        lst.append(a)
    break
print(lst)
