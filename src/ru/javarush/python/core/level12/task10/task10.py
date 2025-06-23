# Запись бинарных данных

# Напишите программу, которая читает изображение input_image.jpg и записывает его в другой файл output_image.jpg.

# Напишите тут ваш код
with open('input_image.jpg', 'rb') as in_image:
    image = in_image.read()

with open('output_image.jpg', 'wb') as out_image:
    out_image.write(image)

