# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data:
    dates = []

    @classmethod
    def convert_int(cls, date):
        cls.dates = date.split('-')
        day, month, year = [int(i) for i in cls.dates]
        print(day, month, year)  # Для проверки
        return day, month, year

    @staticmethod
    def validation(date):
        day, month, year = [int(i) for i in date.split('-')]
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2021 >= year >= 0:
                    print(day, month, year)  # Для проверки
                    return day, month, year
                else:
                    print('Неверный год')
            else:
                print('Неверный месяц')
        else:
            print('Неверный день')


Data.convert_int('31-12-2020')
Data.validation('33-12-2020')
