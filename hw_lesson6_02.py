# 2. Реализовать класс Road (дорога),
# в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
#  толщиной в 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500

# Task is ready

class Road:
    _length: int
    _width: int

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculation(self, weight, thikness):
        self.weight = weight
        self.thikness = thikness
        return self._length * self._width * self.weight * self.thikness


sample = Road(100, 20)
print(f"Масса асфальта равна {sample.calculation(25, 4)} кг")