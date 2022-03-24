# Дана строка из пяти целых чисел, разделенных пробелом.
# Пример входных данных: "2 12 -45 7 10"
# Напишите программу, которая находит среди них минимальное положительное число.
# Если таких чисел несколько - вывести любое из них.

# При решении задачи требуется учесть формат входных данных.
# Если входные данные некорректные, сообщить об этом.

while True:
    line = input("Введите пять целых чисел: ")
    line_list = line.split(" ")
    number_list = []
    try:
        for number in line_list:
            number_list.append(int(number))
        if len(number_list) > 5:
            raise ValueError
        break
    except ValueError:
        print("Данные некорректные. Попробуйте ввести их снова.")

min_positive = number_list[0]
for number in number_list:
    if 0 <= number < min_positive:
        min_positive = number
if min_positive >= 0:
    print("Минимальное положительное число из введенных", min_positive)
else:
    print("Вы не ввели положительных чисел")
