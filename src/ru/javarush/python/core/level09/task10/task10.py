# Рычащие.

# Создайте базовый класс Animal с методом speak, который возвращает строку "Ррррр!".
# Затем создайте дочерний класс Dog, который будет наследовать от Animal и переопределять метод speak,
# добавляя к поведению родительского класса собственное поведение с использованием метода super().

# Напишите тут ваш код
class Animal:
    def speak(self):
        return 'Ррррр!'

class Dog(Animal):
    def speak(self):
        animal = super().speak()
        return f'Animal speak {animal} Гав!'

dog = Dog()
print(dog.speak())