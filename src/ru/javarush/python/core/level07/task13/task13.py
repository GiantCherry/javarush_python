# Обход словаря.

# Напишите программу, которая создает словарь с информацией о человеке (например, имя, возраст, адрес, и контактная информация).
# Программа должна:
# Перебрать все элементы словаря, включая вложенные словари, с использованием циклов.
# Реализовать функцию для обхода всех уровней вложенности и вывода ключей и значений.

# Напишите тут ваш код
def person_print(person, indent=0):
    for key, value in person.items():
        print('  ' * indent + f"{key}: ", end="")
        if isinstance(value, dict):
            print()
            person_print(value, indent + 1)
        else:
            print(value)


person = {
    "name": "John Doe",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "CA",
        "postal_code": "12345"
    },
    "contact": {
        "email": "john.doe@example.com",
        "phone": {
            "home": "555-1234",
            "work": "555-5678"
        }
    }
}

person_print(person)