# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here

import random

n = int(input("Число элементов в списке: "))
numbers = []

i = 1
while i <= n:
    numbers.append(random.randint(-100, 100))
    i += 1

summa = 0
for el in numbers:
    if el > 0 and el % 2 == 0:
        summa += el

print(numbers)
print(summa)
