# Даны номер месяца и номер года. Найдите сколько дней в этом месяце.
# При вводе неверного номера месяца или некорректного значения программа должна сообщить об ошибке
# и попросить ввести корректные данные. Также необходимо учесть високосный или не високосный год.
# Алгоритм проверки на високосный год оформите в виде отдельной функции.
#
# Входная строка содержит два целых числа – номер месяца (возможно, неправильный) и номер года.

def is_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 == 0 and year % 400 != 0:
        return False
    return True


while True:
    line = input("Введите номер месяца и номер года через пробел: ")
    try:
        month, year = line.split(" ")
        month = int(month)
        year = int(year)
        if month < 1 or month > 12:
            raise ValueError
        break
    except (ValueError, TypeError):
        print("Data are incorrect")

if month in (1, 3, 5, 7, 8, 10, 12):
    print("В этом месяце 31 день")
elif month == 2 and is_leap(year):
    print("В этом месяце 29 дней")
elif month == 2 and not is_leap(year):
    print("В этом месяце 28 дней")
else:
    print("В этом месяце 30 дней")
