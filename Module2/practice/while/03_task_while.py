# По данному натуральному n выведите лесенку из n ступенек, i-я ступень состоит из чисел от 1 до i без пробелов.
# Формат входных данных: Вводится натуральное число n.
# Формат выходных данных: Выведите ответ на задачу.
# Пример:
# Для n = 4
# Нужно вывести:
# 1
# 12
# 123
# 1234

# TODO: your code here

n = int(input("n: "))
a = 1

while a <= n:
    b = 1
    line = ""
    while b <= a:
       line = line + str(b)
       b += 1
    print(line)
    a += 1
