# Проверить, является ли заданная строка доменным именем для протоколов http или https, с необязательным слешем в конце.
# Специальные символы не используются.
# Примеры:
# http://example.com/ — Да(является)
# example.com — Нет
# https://кремль.рф — Да

import re

text_list = ["http://re.re",
        "https://re/re",
        "https://кремль.рф",
        "example.com"]

pattern1 = r"http://\w+[.]\w+"
pattern2 = r"https://\w+[.]\w+"

for text in text_list:
    if re.fullmatch(pattern1, text) or re.fullmatch(pattern2, text):
        print("Yes")
    else:
        print("No")
