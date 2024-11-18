from datetime import datetime

try:
    print('Введите дату отправления в формате ДД/ММ/ГГ ЧЧ:ММ')
    start_date = datetime.strptime(input(), "%d/%m/%y %H:%M")
except ValueError:
    print("Неверный формат")
    exit()
try:
    print('Введите дату прибытия в формате ДД/ММ/ГГ ЧЧ:ММ')
    final_date = datetime.strptime(input(), "%d/%m/%y %H:%M")
except ValueError:
    print("Неверный формат")
    exit()
if final_date < start_date:
    print("Дата прибытия должны быть позже даты отправки")
    exit()
travel_time = final_date - start_date
print("Вы будете в пути: ", travel_time)