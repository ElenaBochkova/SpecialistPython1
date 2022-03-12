# Напишите функцию,  определяющую является ли число палиндромом.
# Палиндром - число читающееся одинаково слева направо и справа налево.
# Пример палиндрома: 34543
# * попробуйте решить данную задачу, не преобразуя число к строке

def my_len(number):
    for i in range(1, number):
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



# Тестируем функцию
print(palindrome(3454))
print(palindrome(3443))
print(palindrome(1234541))
print(palindrome(1234321))
print(palindrome(77777))
