# Автопарк.

# Напишите функцию check_subclass для проверки, является ли один класс подклассом другого.
# Используйте функцию issubclass() для выполнения проверки.
# Затем создайте классы Vehicle, Car, Bicycle, и проверьте, являются ли Car и Bicycle подклассами Vehicle.

# Напишите тут ваш код
def check_subclass(class_a, class_b):
    return issubclass(class_a, class_b)

class Vehicle:
    pass

class Car(Vehicle):
    pass

class Bicycle(Vehicle):
    pass

vehicles = [Vehicle, Car, Bicycle]

for vehicle in vehicles:
    print(check_subclass(vehicle, Vehicle))