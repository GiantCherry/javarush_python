# Символы в строке

# Напишите программу, которая принимает строку от пользователя, выводит ее длину,
# а затем запрашивает у пользователя индекс.
# Программа должна вывести символ строки по этому индексу.
# Если индекс выходит за пределы строки, программа должна вывести соответствующее сообщение.

# Напишите тут ваш код
user_srt = input("Введите строку: ")

len_str = len(user_srt)
print(len_str)

index = int(input("Введите индекс: "))
if index > len_str - 1:
    print("Вышли за пределы строки.")
else:
    print(user_srt[index])

