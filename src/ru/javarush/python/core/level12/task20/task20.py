# Исключение несериализуемых полей

# Напишите класс, который содержит несериализуемые поля, такие как открытые файлы или базы данных,
# и реализуйте методы __getstate__() и __setstate__(),
# чтобы исключить эти поля при сериализации и восстановить их при десериализации.

# Напишите тут ваш код
import pickle

class MyClass:
    def __init__(self, filepath):
        self.filepath = filepath
        self.file = open(filepath, 'r')
        self.data = self.file.read()

    def __getstate__(self):
        state = self.__dict__.copy()
        # Remove the file attribute from the state to prevent serialization
        del state['file']
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        # Re-open the file upon deserialization
        self.file = open(self.filepath, 'r')
        self.data = self.file.read()

    def __del__(self):
        self.file.close()


# Example usage:
obj = MyClass('example.txt')
serialized_obj = pickle.dumps(obj)
print(serialized_obj)

deserialized_obj = pickle.loads(serialized_obj)
print(deserialized_obj.data)