# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def func(name, surname, city, year, email, phone):
    return f'Имя: {name}; Фамилия: {surname}; Город проживания: {city}; Год рождения: {year}; ' \
           f'Email: {email}; Телефон: {phone}.'


lst = (input('Введите имя, фамилию, год рождения, город проживания, email и телефон через пробел: ')).split()
name, surname, city, year, email, phone = lst
print(func(name, surname, city, year, email, phone))

