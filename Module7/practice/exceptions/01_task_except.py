# Дан прямоугольник размером n×m. Напишите программу, вычисляющую, сколько квадратов
# со стороной m от него получится отрезать.

# На вход программе подается строка формата nxm (x - латинская буква икс).
# Пример входных данных: 12x6
# Если данные вводятся в неверном формате, сообщить об этом и запросить ввод заново.

def validate(a, b):
    try:
        a = int(a)
        b = int(b)
        return a, b
    except ValueError:
        print("Data cannot be transformed to int")


while True:
    line = input("Data: ")
    try:
        a, b = line.split("x")
        a, b = validate(a, b)
        print("Квадратов:", a // b)
        break
    except ValueError:
        print("Data are incorrect")
    except TypeError:
        print("Data are incorrect")
