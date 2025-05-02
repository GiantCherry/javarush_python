# Создаем объекты.

# Создайте класс Car с атрибутами make, model и year.
# Добавьте метод display_info(), который выводит информацию о машине.
# Затем создайте объект этого класса и вызовите метод display_info().

# Напишите тут ваш код
class Car:
    make = 'make'
    model = 'model'
    year = 'year'

    def display_info(self):
        print(f'Car\'s info: {self.make}, {self.model}, {self.year}!')

car = Car()
car.display_info()