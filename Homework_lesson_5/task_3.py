# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('for_task_3.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    m = 0
    for line in range(len(lines)):
        if line > m:
            m = line
        r = line + 1
    for line_2 in lines:
        last_name, name, salary, cur = line_2.split()
        salary = int(salary)
        a_salary = salary * r / r / 1000
        if salary > 20000:
            print(f'У сотрудника {last_name} {name} оклад менее 20 тыс. руб.')

print(f'\nСредняя зарплата сотрудников составляет {a_salary} тыс. руб.')
