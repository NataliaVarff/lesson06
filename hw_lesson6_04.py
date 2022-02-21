# 4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат

# Task ready

class Car:
    speed: int
    color: str
    name: str
    is_police: bool

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def info(self):
        print(f"Машина марки {self.name}, цветом {self.color} и со скоростью {self.speed}")

    def go(self):
        if self.speed != 0:
            print("машина поехала")

    def stop(self):
        if self.speed == 0:
            print("машина остановилась")

    def turn(self, direction:int):
        if direction == 1:
            print(f"машина повернула налево")
        if direction == 2:
            print("машина повернула направо")

    def show_speed(self):
        print(f"скорость машины {self.speed}")

class TownCar(Car):
    speed: int
    color: str
    name: str
    is_police: bool

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        if self.speed > 60:
            print(f"Машина превышает скорость 60 км/ч. Текущая скорость {self.speed}")

class SportCar(Car):
    speed: int
    color: str
    name: str
    is_police: bool

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

class WorkCar(Car):
    speed: int
    color: str
    name: str
    is_police: bool

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        if self.speed > 40:
            print(f"Машина превышает скорость 40 км/ч. Текущая скорость {self.speed}")
        else:
            print(f"Машина не превышает скорость 40 км/ч. Текущая скорость {self.speed}")


class PoliceCar(Car):
    speed: int
    color: str
    name: str
    is_police: bool

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

car1 = Car(10, "green", "toyota", False )
car1.info()
car1.go()
car1.stop()
car1.turn(2)
car1.show_speed()

carT = TownCar(70, "yellow", "kia", False)
carT.info()
carT.go()
carT.stop()
carT.show_speed()

carS = SportCar(250, "red", "ferrari", False)
carS.info()
carS.go()
carS.turn(2)
carS.show_speed()

carW = WorkCar(30, "black", "ford", False)
carW.info()
carW.show_speed()

carP = PoliceCar(100, "blue", "lada", True)
carP.info()
carP.go()
carP.stop()
carP.show_speed()

