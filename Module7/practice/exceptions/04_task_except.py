# Даны два уравнения прямых вида у=kx+b и виде строки. Проверить, пересекаются ли данные прямые?
# Примеры уравнений: "y = 2x + 4"  "y = -12x -12"

# Проверьте входные данные на корректность

def extract_equation(line, i = 0):
    try:
        two_sides = line.split("=")
        res = two_sides[i].strip().replace(" ", "")
        return res
    except (ValueError, TypeError):
        raise ValueError


def extract_y(line):
    try:
        y = extract_equation(line, 0)
        if y == 'y':
            return True
    except ValueError:
        return False


def x_pos(line):
    try:
        second = extract_equation(line, 1)
        pos = second.find('x')
        if pos != -1:
            return pos, second
        else:
            raise ValueError
    except ValueError:
        raise ValueError


def extract_k(line):
    try:
        pos, second = x_pos(line)
        if pos == 0:
            return 1
        else:
            return int(second[0:pos])
    except ValueError:
        return False


def extract_b(line):
    try:
        pos, second = x_pos(line)
        b = int(second[pos+1:].strip())
        return b
    except ValueError:
        return False


def get_equation():
    while True:
        line = input("Введите уравнение прямой в формате y = kx + b: ")
        if extract_y(line) and extract_k(line) and extract_b(line):
            return extract_k(line), extract_b(line)
        else:
            print("Ваше уравнение не распознано. Попробуйте еще раз")


def solve_equations(k1, b1, k2, b2):
    if (k1 - k2) == 0:
        return False
    else:
        x = (b2 - b1)/(k1 - k2)
        return x, k1 * x + b1


k1, b1 = get_equation()
k2, b2 = get_equation()
if solve_equations(k1, b1, k2, b2):
    x, y = solve_equations(k1, b1, k2, b2)
    print(f"Прямые пересекаются в точке x = {round(x,2)}, y = {round(y,2)}")
else:
    print("Прямые параллельны")
