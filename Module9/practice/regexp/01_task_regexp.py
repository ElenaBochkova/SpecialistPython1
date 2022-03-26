# Дано произвольное предложение. Слова разделены пробелами. Предложение содержит знаки препинания.
# Найдите:
# 1) первое слово из строки
# 2) первые два символа каждого слова
# 3) все слова начинающиеся на гласную букву
# 4) все слова начинающиеся на согласную букву
# 5) все уникальные(без дубликатов) знаки препинания

# 5) все уникальные(без дубликатов) знаки препинания
import re

text = "Lorem ipsum dolor sit amet; consectetur adipiscing elit. Fusce dolor turpis, condimentum id molestie sit amet, dignissim et quam. Quisque in purus eu lorem finibus gravida ut ultricies dolor. Nam eu condimentum arcu, at pellentesque nisi. Nullam id dictum dui, quis sodales dolor. Morbi ornare et magna at vehicula. Nunc blandit nec tortor tincidunt consequat. Suspendisse sit amet elementum dolor, non condimentum est. Sed vestibulum justo nulla, in vehicula neque volutpat ac. Suspendisse potenti. Aenean ut mauris accumsan, molestie leo non, ultrices purus. Fusce eget ullamcorper tellus, sed porttitor mauris. Morbi laoreet lorem ut viverra facilisis. Morbi vitae magna orci."
print("Первые слова из строки", re.findall(r'\b[A-Z]\w+\b', text))
print("Первые два символа из каждого слова", re.findall(r'\b\w{2}', text))
print("Все слова, начинающиеся на гласную букву", re.findall(r"\b[aeuioAEUIO]\w+\b", text))
print("Все слова, начинающиеся на согласную букву", re.findall(r"\b[^ aeuioAEUIO]\w+\b", text))
types = re.findall(r"[.,:;!?-]", text)
unique_types = []
for el in types:
    if el not in unique_types:
        unique_types.append(el)
print("Уникальные знаки препинания", unique_types)
