# Дана строка текста, слова разделены пробелами, знаки препинания отсутствуют.
# Определить в предоставленном сообщении количество слов длиной больше, чем 5.

text = "Lorem ipsum dolor sit amet consectetur adipiscing elit Integer porttitor bibendum nisi ut convallis ante"
# Примечание: для генериации текста можете воспользоваться сайтом: https://ru.lipsum.com/

index = 1
count = 0

while index != len(text):
    index = text.find(" ")
    if index == -1:
        index = len(text)
        word = text
    else:
        word = text[:index]
    if len(word) > 5:
        count += 1
    text = text[index+1:]

print(count)
