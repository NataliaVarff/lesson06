# 3. Реализовать базовый класс Worker (работник),
# в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным
# и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).

# Task ready

class Worker:
    name: str
    surname: str
    position: str
    _income: {}

# income = {"wage": wage, "bonus": bonus}
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": 100, "bonus": 25}


class Position(Worker):

    def __init__(self, name, surname, position):
        super().__init__(name, surname, position)

    def get_fullname(self):
        return f"{self.name} {self.surname}"

    def get_totalincome(self):
        return self._income["wage"] + self._income["bonus"]

employee = Position("Tom", "York", "engineer")
print(employee.get_fullname())
print(employee.get_totalincome())


