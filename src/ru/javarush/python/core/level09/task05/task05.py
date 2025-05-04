# Защищайтесь.

# Создайте класс Car, который будет иметь публичный атрибут brand и защищенный атрибут _model_.
# Добавьте методы для получения и установки значения защищенного атрибута _model.
# Создайте объект класса Car, установите значения атрибутов и выведите их на экран.

# Напишите тут ваш код
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self._model_ = model

    def set_model(self, model):
        self._model_ = model

    def get_model(self):
        return self._model_


car = Car('Honda', 'Accord')
print(f'{car.brand} - {car.get_model()}')

car.brand = 'BMW'
car.set_model('X5')
print(f'{car.brand} - {car.get_model()}')