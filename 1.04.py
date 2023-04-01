import csv


# Создаем списки для заголовков и строк
header = ["#", "Понедельник", "", "Вторник", "", "Среда", "", "Четверг", "", "Пятница", "", "Суббота"]
rows = []

# Читаем данные из исходного файла и заполняем соответствующие списки
with open("schedule.csv", encoding="utf-8", newline="") as file:
    reader = csv.reader(file, delimiter=",")
    # Пропускаем первую строку (заголовки столбцов)
    next(reader)
    # Добавляем строки со значениями в список
    for i, row in enumerate(reader, start=1):
        rows.append([str(i)] + row)

# Записываем данные в новый файл в текстовом формате
with open("result.txt", mode="w", encoding="utf-8") as file:
    # Записываем заголовки
    file.write(" ".join(header) + "\n")
    # Записываем строки
    for row in rows:
        file.write("  ".join(row) + "\n")