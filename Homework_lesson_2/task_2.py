# lst = [1, 2, 3, 4, 5, 6]

i = int(input('Введите размер списка: '))
lst = []
for el in range(i):
    lst.extend(input('Введите элемент: '))
print(lst)

el_2 = 0
for el_3 in range(int(len(lst)/2)):
    lst[el_2], lst[el_2 + 1] = lst[el_2 + 1], lst[el_2]
    el_2 += 2
print(lst)
