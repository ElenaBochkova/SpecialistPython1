# Дан файл data/info.txt, в каждой строке которого содержится строка или целое число
# Найдите сумму всех чисел, пропуская все строки содержащие не числовые значения

sum = 0
with open("data/info.txt", "r") as f:
    for line in f:
        try:
            number = int(line)
        except ValueError:
            number = 0
        sum += number

print(sum)
