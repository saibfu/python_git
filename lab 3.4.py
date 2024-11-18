from datetime import datetime, timedelta

try:
    print('Введите дату рождения в формате ДД/ММ/ГГ')
    hb_date = datetime.strptime(input(), "%d/%m/%y")
except ValueError:
    print("Неверный формат")
    exit()

days = 10000
minutes = 1000000
seconds = 1000000000

pr_days = timedelta(days=days)
pr_minutes = timedelta(minutes=minutes)
pr_seconds = timedelta(seconds=seconds)

new_days = hb_date + pr_days
new_minutes = hb_date + pr_minutes
new_seconds = hb_date + pr_seconds

print("10.000 дней будет: ", new_days)
print("1.000.000 минут будет: ", new_minutes)
print("1.000.000.000 секунд будет: ", new_seconds)
