# Дан список имен.
# Выведите все имена в одну строку через запятую

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

# TODO: your code here
names_in_line = ""

for el in names:
    if names_in_line != "":
        names_in_line += ", "
    names_in_line += el

print(names_in_line)

# Пример вывода:
# Иван, Ирина, Вячеслав, Василий, Петр
