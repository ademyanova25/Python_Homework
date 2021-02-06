# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('for_task_5.txt', 'w', encoding='utf-8') as f:
    f.write(input('Введите набор чисел, разделенных пробелами: '))
with open('for_task_5.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        lst = line.split()
        for i, item in enumerate(lst):
            lst[i] = int(item)
        s = sum(lst)
        print(s)

