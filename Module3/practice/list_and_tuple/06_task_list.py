# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число

# TODO: your code here
my_list = []

i = first_number + 1

while i < second_number:
    if i % 3 == 0:
        my_list.append(i)
    i += 1

print(my_list)
