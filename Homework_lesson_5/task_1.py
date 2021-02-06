 # Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
 # Об окончании ввода данных свидетельствует пустая строка.


with open('My_file.txt', 'w', encoding='utf-8') as f:
    f.write(input('Введите построчно данные: '))

while True:
    s = input('Введите построчно данные: ')
    with open('My_file.txt', 'a', encoding='utf-8') as f:
        f.write(f"\n{s}")
        if not s:
            break
