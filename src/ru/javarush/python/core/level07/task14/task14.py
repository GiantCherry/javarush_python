# В глубинах самых глубин.

# Напишите программу, которая создает словарь с информацией о человеке (например, имя, возраст, адрес, и контактная информация).
# Программа должна:
# Изменить значения верхнего уровня, вложенного словаря и более глубокого уровня вложенности.
# Добавить новый элемент во вложенный словарь.
# Удалить элемент из вложенного словаря и верхнего уровня.

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

person['name'] = 'Danya Lunev'
person['address']['city'] = 'Moscow'
person['contact']['telegram'] = '@denlunev'
del person['address']['state']
del person['age']

person_print(person)