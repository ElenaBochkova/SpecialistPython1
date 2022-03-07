# Дана строка текста, слова разделены пробелами.
# В предложении могут присутствовать следующие знаки препинания ",.!?-". Знаки препинания частьюслова не являются.
# Определить в предоставленном сообщении количество слов длиной больше, чем 7.

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam placerat consequat vestibulum. " \
       "Donec tincidunt sed lorem et feugiat. Nullam elementum"
# Примечание: для генериации текста можете воспользоваться сайтом: https://ru.lipsum.com/
# Примечание: обратите внимание на перенос длинной строки на новую строку

# TODO: your code here

text = text.replace(",","").replace(".","").replace("!", "").replace("?", "").replace(" - "," ").replace("\n", " ")

index = 1
count = 0

while index != len(text):
    index = text.find(" ")
    if index == -1:
        index = len(text)
        word = text
    else:
        word = text[:index]
    if len(word) > 7:
        count += 1
        print(word)
    text = text[index+1:]

print(count)
