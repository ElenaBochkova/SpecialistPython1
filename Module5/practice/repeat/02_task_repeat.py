# Является ли палиндромом?
# Напишите функцию, проверяющую является ли число палиндромом.
# палиндром - число одинаково читающееся слева направо, так и справа налево.
#  Пример палиндрома: 12321

def my_len(number):
    for i in range(number):
        if number // 10 ** i == 0:
            return i
    return 0


def palindrome(number):
    while my_len(number) > 0:
        first = number // 10 ** (my_len(number) - 1)
        second = number % 10
        if first != second:
            return False
        number = number - first * (10 ** (my_len(number) - 1))
        number = number // 10
    return True

print(palindrome(12321))
