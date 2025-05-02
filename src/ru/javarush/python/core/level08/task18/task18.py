# Timezone.

# Напишите программу, которая конвертирует текущее время из часового пояса UTC в заданный пользователем часовой пояс.
# Программа должна:
# Получить текущее время в часовом поясе UTC.
# Запросить у пользователя смещение в часах относительно UTC.
# Создать объект часового пояса с заданным смещением.
# Конвертировать текущее время в заданный часовой пояс.
# Вывести текущее время в UTC и в заданном часовом поясе.

# Напишите тут ваш код
'''
import datetime

# now = datetime.datetime.utcnow()
now = datetime.datetime.now(datetime.UTC)

hour = int(input('Введите смещение в часах: '))

new_time = datetime.timezone(datetime.timedelta(hours=hour))
new_time_dt = now.astimezone(new_time)

print(now)
print(new_time_dt)
'''

from datetime import datetime, timedelta, timezone

# Получить текущее время в часовом поясе UTC
current_utc_time = datetime.now(timezone.utc)

# Запросить у пользователя смещение в часах относительно UTC
offset_hours = int(input("Введите смещение относительно UTC в часах: "))

# Создать объект часового пояса с заданным смещением
user_timezone = timezone(timedelta(hours=offset_hours))

# Конвертировать текущее время в заданный часовой пояс
current_user_time = current_utc_time.astimezone(user_timezone)

# Вывести текущее время в UTC и в заданном пользователем часовом поясе
print("Текущее время в UTC:", current_utc_time)
print(f"Текущее время в часовой зоне с смещением {offset_hours} час(ов):", current_user_time)