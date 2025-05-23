# Супер-экшен.

# Создайте два базовых класса BaseA и BaseB, каждый из которых имеет метод action().
# Создайте производный класс Derived с переопределенным методом action(), который вызывает метод super().action().
# Вызовите метод action() у объекта класса Derived и проанализируйте порядок вызова методов.

# Напишите тут ваш код
class BaseA:
    def action(self):
        print('Action BaseA')

class BaseB:
    def action(self):
        print('Action BaseB')

class Derived(BaseA, BaseB):
    def action(self):
        print('Action Derived')
        super().action()


derived = Derived()
derived.action()

