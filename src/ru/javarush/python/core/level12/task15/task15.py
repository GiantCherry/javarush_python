# Сериализация помощью pickle

# Напишите тут ваш код
import pickle

student_info = {
    'name': 'John Doe',
    'age': 20,
    'status': 'student'
}

# Напишите тут ваш код
with open('data.pkl', 'wb') as file:
    pickle.dump(student_info, file)

with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)
