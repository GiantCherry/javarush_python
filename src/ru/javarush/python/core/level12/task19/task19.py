# Использованиее метода reduce()

# Напишите класс, который управляет своей сериализацией с помощью метода __reduce__(),
# чтобы при сериализации и десериализации сохранялись только определенные поля.

# Напишите тут ваш код
import pickle

class CustomSerializable:
    def __init__(self, name, age, password, hidden_info):
        self.name = name
        self.age = age
        self.password = password
        self.hidden_info = hidden_info

    def __reduce__(self):
        return self._serialize, (self.name, self.age)

    @staticmethod
    def _serialize(name, age):
        return CustomSerializable(name, age, None, None)

# Создание объекта
obj = CustomSerializable("John Doe", 30, "supersecret", "hidden")

# Сериализация
serialized_obj = pickle.dumps(obj)

# Десериализация
deserialized_obj = pickle.loads(serialized_obj)

# Проверка
print(f"Name: {deserialized_obj.name}, Age: {deserialized_obj.age}")
print(f"Password: {deserialized_obj.password}, Hidden Info: {deserialized_obj.hidden_info}")