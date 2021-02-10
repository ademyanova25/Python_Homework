# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        if self.speed != 0:
            return f'Машина {self.name} едет.'

    def stop(self):
        if self.speed == 0:
            return f'Машина {self.name} остановилась.'

    def turn(self, side):
        return f'Машина {self.name} повернула {side}.'

    def show_speed(self):
        return f'Текущая скорость составляет {self.speed}.'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Вы превсили скорость! Ваша скорость {self.speed}.'
        else:
            return f'Ваша скорость {self.speed} в пределах нормы.'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Вы превысили скорость! Ваша скорость {self.speed}.'
        else:
            return f'Ваша скорость {self.speed} в пределах нормы.'


class PoliceCar(Car):
    pass


town = TownCar(66, 'blue', 'Nissan', False)
sport = SportCar(130, 'black', 'Mercedes', False)
work = WorkCar(0, 'black', 'Audi', False)
police = PoliceCar(90, 'white', 'Lada', True)

print(town.go(), town.show_speed())
print(work.stop())
print(police.go(), police.turn('направо'))
print(sport.go(), sport.show_speed())
