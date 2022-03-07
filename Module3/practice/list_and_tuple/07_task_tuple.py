# Дан кортеж заполненный целыми числами
# Найдите самый большой элемент кортежа
tup = (2, 4, 6, -4, 12, 0, 5)

# TODO: your code here

maxim = tup[0]

for el in tup:
    if maxim < el:
        maxim = el

print(maxim)
