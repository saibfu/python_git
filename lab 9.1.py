participants = {
    "Иванов" : 20,
    "Сидоров" : 68,
    "Петров" : 26,
    "Смирнов" : 68
}

participants["Макаров"] = 74

values = participants.values()
srsnach = sum(values) / len(values)

for name, points in participants.items():
    if points > srsnach:
        print(name, end=" ")
print()
min_points = min(values)
print(min_points, end=": ")
for name, points in participants.items():
    if points == min_points:
        print(name, end=" ")
print()
max_points = max(values)
print(max_points, end=": ")
for name, points in participants.items():
    if points == max_points:
        print(name, end=" ")
print()
print("Средний балл:", srsnach)