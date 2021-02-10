# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.

# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.

from time import sleep


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        # Проверка
        lst = ['Красный', 'Желтый', 'Зеленый']
        lst_check = []
        for el in self.__color:
            if el == 'Красный':
                lst_check.append(el)
            elif el == 'Желтый':
                lst_check.append(el)
            else:
                lst_check.append(el)
        while True:
            if lst != lst_check:
                break
        # Бесконечный светофор
            else:
                print(self.__color[0])
                sleep(7)
                print(self.__color[1])
                sleep(2)
                print(self.__color[2])
                sleep(10)

    # Другой вариант

    # def running(self):
    #     while True:
    #         for el in self.__color:
    #             if el == 'Красный':
    #                 print('Красный')
    #                 sleep(7)
    #             elif el == 'Желтый':
    #                 print('Желтый')
    #                 sleep(2)
    #             else:
    #                 lst.append(el)
    #                 sleep(10)


tl = TrafficLight()
tl.running()
