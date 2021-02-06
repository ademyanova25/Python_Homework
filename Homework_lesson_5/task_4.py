# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

d = {
    '1': 'Один',
    '2': 'Два',
    '3': 'Три',
    '4': 'Четыре',
}
with open('for_task_4.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    with open('for_task_4_2.txt', 'w', encoding='utf-8') as f:
        for line in lines:
            for line_2 in lines:
                number, number_2, number_3 = line_2.split()
                if d[number_3]:
                    number = d[number_3]
                    w = f'{number} {number_2} {number_3}\n'
                    f.writelines(w)
            break






