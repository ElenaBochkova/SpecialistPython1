# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

name_length = 0
the_longest = ""

for el in names:
    if len(el) > name_length:
        the_longest = el
        name_length = len(el)

print(the_longest)

# TODO: your code here
