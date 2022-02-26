# Дано целое число m, задающее номер месяца года.
# Выведите строку — название времени года, соответствующего данному месяцу.
# Формат входных данных: дано целое число m (1 ≤ m ≤ 12).
# Формат выходных данных: требуется вывести название времени года

# TODO: your code here

month = int(input("Введите номер месяца: "))

if month > 2 and month < 6:
    print("Spring")
elif month > 5 and month < 9:
    print("Summer")
elif month > 8 and month < 12:
    print("Autumn")
else:
    print("Winter")
