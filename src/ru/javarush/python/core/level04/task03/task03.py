# Мешанина

# Напишите программу, которая запрашивает у пользователя целое число, вещественное число и строку.
# Затем преобразуйте целое число в вещественное, вещественное число в строку, и строку в целое число (если это возможно).
# Выведите результаты преобразований и их типы.

# Напишите тут ваш код
int_var = int(input("Введите целое число: "))
float_var = float(input("Введите вещественное число: "))
str_var = input("Введите строку: ")

int_to_float = float(int_var)
float_to_str = str(float_var)
str_to_int = int(str_var)

print(int_to_float, type(int_to_float))
print(float_to_str, type(float_to_str))
print(str_to_int, type(str_to_int))
