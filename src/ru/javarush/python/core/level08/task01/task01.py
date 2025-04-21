# Системные функции.

# Напишите программу, которая создает несколько объектов различных типов и
# использует функции id(), hash(), и dir() для выполнения следующих операций:
# Определить и вывести уникальные идентификаторы объектов с помощью id().
# Вывести хеш-значения хешируемых объектов с помощью hash().
# Вывести список атрибутов и методов объекта с помощью dir().

# Напишите тут ваш код
str_obj = 'String'
int_obj = 23
float_obj = 23.1

class ClassObj:
    str_obj = 'String'
    int_obj = 23
    float_obj = 23.1

class_obj = ClassObj()

print(id(str_obj), id(int_obj), id(float_obj), id(class_obj))
print(hash(str_obj), hash(int_obj), hash(float_obj))
print(dir(str_obj), dir(int_obj), dir(float_obj), dir(class_obj))
