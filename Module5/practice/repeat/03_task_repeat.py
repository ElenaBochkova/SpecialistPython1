# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.

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

a = 1
b = 1000
count = 0
for n in range (a, b+1):
    if palindrome(n):
        count += 1
print(count)
