# Используя функцию average() из предыдущей задачи, найдите среднее арифметическое всех элементов списка и кортежа

def average(*args):
    if len(args) > 0:
        s = 0
        for el in args:
            s += el
        return s / len(args)
    return 0


def gen_list(size, at=-10, to=10):
    import random  # импорт в функции возможен, но не рекомендуется PEP-8
    """
    :param size: кол-во элементов списка
    :param at: минимально возможное значение элементов
    :param to: максимально возможное значение элементов
    :return: списко из size произвольных элементов вдиапазоне at..to 
    """
    result_list = []
    for _ in range(size):
        result_list.append(random.randint(at, to))
    return result_list


my_list = gen_list(10)

print("Average:", average(*my_list))

my_tuple = 5, 7, -4, 10, 8

print("Average:", average(*my_tuple))
