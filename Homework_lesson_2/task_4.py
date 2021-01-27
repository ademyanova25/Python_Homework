a = input('Введите несколько слов через проблемы: ')
lst = a.split()
for i, el in enumerate(lst, 1):
    print(i, el[:10])
