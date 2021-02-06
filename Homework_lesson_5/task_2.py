# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.

with open('for_task_2.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    m = 0
    for line in range(len(lines)):
        if line > m:
            m = line
    r = line+1
    print(f'В данной файле {r} строк(и).\n')

    for i, line in enumerate(lines):
        n = len(line.split())
        print(f'В строке № {i+1} находятся {n} слов(а).')


