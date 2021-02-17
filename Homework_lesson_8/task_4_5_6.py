# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, Xerox). В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
# Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.
# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

'''Объединила все три задания в одно + добавила где-то свою логику.'''


class Warehouse(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class ReceivingError(Warehouse):
    def __init__(self, text):
        self.text = f'Невозможно добавить товар на склад:\n {text}'


class TransferError(Warehouse):
    def __init__(self, text):
        self.text = f'Невозможно получить товар. Товара нет на склад:\n {text}'


class ValidationError(Warehouse):
    def __init__(self, text):
        self.text = f'Невозможно добавить товар:\n {text}'


class Warehouse:
    def __init__(self):
        self.warehouse = []
        self.lst_printer = []
        self.lst_scanner = []
        self.lst_xerox = []
        self.count_warehouse = 0
        self.count_printer = 0
        self.count_scanner = 0
        self.count_xerox = 0

    def receiving(self, equipment):
        # Проверка на тип
        if not isinstance(equipment, OfficeEquipment):
            raise ReceivingError(f"{equipment} не оргтехника")
        equip_type, model, number, count = str(equipment).split('-')
        count = int(count)
        if equip_type == 'Printer':
            self.lst_printer.append([equip_type, model, number, count])
            self.warehouse.append([equip_type, model, number, count])
            self.count_printer += count
            self.count_warehouse += count
        elif equip_type == 'Scanner':
            self.lst_scanner.append([equip_type, model, number, count])
            self.warehouse.append([equip_type, model, number, count])
            self.count_scanner += count
            self.count_warehouse += count
        else:
            self.lst_xerox.append([equip_type, model, number, count])
            self.warehouse.append([equip_type, model, number, count])
            self.count_xerox += count
            self.count_warehouse += count
        print(f'Товар {equip_type} в размере {count} единиц добавлен на склад.')

    def transfer(self, equipment):
        division = []
        equip_type, model, number, count = str(equipment).split('-')
        count = int(count)
        b = 0
        # Проверка на наличие по модели. Раздельно специально (для идентификации чего именно нет - модели или номера).
        while b <= len(self.warehouse):
            for el in self.warehouse:
                if model in el:
                    break
                b += 1
            else:
                raise TransferError(f'{model} нет на складе')
        a = 0
        # Проверка на наличие по номера. Раздельно специально (для идентификации чего именно нет - модели или номера).
        while a <= len(self.warehouse):
            for el in self.warehouse:
                if number in el:
                    break
                a += 1
            else:
                raise TransferError(f'{number} нет на складе')
        # Проверка на колличество техники на складе.
        for i in self.warehouse:
            if i[1] == model:
                if i[2] == number:
                    max_count = i[3]
                    if count > max_count:
                        raise TransferError(f'{model} в колличестве {count} нет на складе. Всего имеется {max_count}')

        if equip_type == 'Printer':
            division.append([equip_type, model, number, count])
            self.lst_printer.remove([equip_type, model, number, count])
            self.warehouse.remove([equip_type, model, number, count])
            self.count_printer -= count
            self.count_warehouse -= count
        elif equip_type == 'Scanner':
            division.append([equip_type, model, number, count])
            self.lst_scanner.remove([equip_type, model, number, count])
            self.warehouse.remove([equip_type, model, number, count])
            self.count_scanner -= count
            self.count_warehouse -= count
        else:
            division.append([equip_type, model, number, count])
            self.lst_xerox.remove([equip_type, model, number, count])
            self.warehouse.remove([equip_type, model, number, count])
            self.count_xerox -= count
            self.count_warehouse -= count
        print(f'Товар {equip_type} в размере {count} единиц(а/ы) передана(о/ы) со склада.')

    def __str__(self):
        return f'На складе сейчас {self.count_warehouse} устройств(а).\n' \
               f'Из них:\n' \
               f'{self.count_printer} принтер(а/ов)\n' \
               f'{self.count_scanner} сканер(а/ов)\n' \
               f'{self.count_xerox} ксерокс(а/ов)'


class OfficeEquipment:
    def __init__(self, model, number, count: int):
        self.model = model
        self.number = number
        self.count = count

    def action(self):
        pass


class Printer(OfficeEquipment):
    def __init__(self, model, number, count: int):
        self.equip_type = 'Printer'
        super().__init__(model, number, count)

    def __str__(self):
        # Валидация на число
        if type(self.count) != int:
            raise ValidationError(f"{self.count} не является числом! Фактический тип: {type({self.count})}.")
        return f'{self.equip_type}-{self.model}-{self.number}-{self.count}'

    def action(self):
        return f'Печать'


class Scanner(OfficeEquipment):
    def __init__(self, model, number, count: int):
        self.equip_type = 'Scanner'
        super().__init__(model, number, count)

    def __str__(self):
        # Валидация на число
        if type(self.count) != int:
            raise ValidationError(f"{self.count} не является числом! Фактический тип: {type({self.count})}.")
        return f'{self.equip_type}-{self.model}-{self.number}-{self.count}'

    def action(self):
        return f'Сканирование'


class Xerox(OfficeEquipment):
    def __init__(self, model, number, count: int):
        self.equip_type = 'Xerox'
        super().__init__(model, number, count)

    def __str__(self):
        # Валидация на число
        if type(self.count) != int:
            raise ValidationError(f"{self.count} не является числом! Фактический тип: {type({self.count})}.")
        return f'{self.equip_type}-{self.model}-{self.number}-{self.count}'

    def action(self):
        return f'Копирование'


warehouse = Warehouse()
xerox_1 = Xerox('Название_1', 'Модель_1', 1)
printer_1 = Printer('Название_2', 'Модель_2', 2)
printer_2 = Printer('Название_3', 'Модель_3', 1)
scanner_1 = Scanner('Название_4', 'Модель_4', 4)
scanner_2 = Scanner('Название_5', 'Модель_5', 1)
printer_3 = Printer('Название_6', 'Модель_6', 5)
printer_4 = Printer('Название_7', 'Модель_7', 3)
xerox_2 = Xerox('Название_8', 'Модель_8', 1)
xerox_3 = Xerox('Название_9', 'Модель_9', 2)
#Для проверки ошибок по трансферу.
xerox_4 = Xerox('Название_10', 'Модель_9', 2)
xerox_5 = Xerox('Название_9', 'Модель_10', 2)
xerox_6 = Xerox('Название_9', 'Модель_10', 3)

warehouse.receiving(xerox_1)
warehouse.receiving(printer_1)
warehouse.receiving(printer_2)
warehouse.receiving(scanner_1)
warehouse.receiving(scanner_2)
warehouse.receiving(printer_3)
warehouse.receiving(printer_4)
warehouse.receiving(xerox_2)
warehouse.receiving(xerox_3)
print(warehouse)
warehouse.transfer(printer_2)
warehouse.transfer(scanner_2)
warehouse.transfer(xerox_3)
print(warehouse)

# Для проверки ошибок по трансферу(закомментировано).

# warehouse.transfer(xerox_4)  # ошибка по модели
# warehouse.transfer(xerox_5)  # ошибка по номеру
# warehouse.transfer(xerox_6)  # ошибка по клличеству
# print(warehouse)

# Для проверки валидации на число(закомментировано).

# xerox_7 = Xerox('Название_1', 'Модель_1', '1')
# warehouse.receiving(xerox_7)
# print(warehouse)
