# Дан текст в котором упоминаются IP-адреса.
# Пример текста:
import re 

text = """
Все публичные сервера и сайты в сети Интернет используют "белые" IP-адреса (например, сайт google.com — 172.217.22.14, 
DNS-сервер Google — 8.8.8.8, сайт yandex.ru — 213.180.204.11, DNS-сервер Яндекс.DNS — 77.88.8.8). 
Все публичные IP-адреса в сети Интернет уникальны и не могут повторяться
"""
# Найдите все упоминаемые IP.
# Точно известно, что все IP-адреса в тексте являются корректными, т.е. не будут встречаться адреса вида 900.400.18.56

pattern = r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}"
print(re.findall(pattern, text))
