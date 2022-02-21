# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.

# TASK ready.
import time


class TrafficLight:
    __color: str

    def __init__(self, color: str):
        self.__color = color

    def runningtest(self):
        print(self.__color)

    def running(self):
        for key, value in self.__color.items():
            time.sleep(value)
            print(key)

traf = TrafficLight(color=
    {"Красный": 7,
     "Желтый": 2,
     "Зеленый": 5
    }
)

traf.running()

stop = TrafficLight("RED")
wait = TrafficLight("YELLOW")
go = TrafficLight("GREEN")

stop.runningtest()
wait.runningtest()
go.runningtest()


