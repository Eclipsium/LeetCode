"""
Реализуйте метод для сжатия повторяющихся символов. Например, строка "aabcccccaaa" 
будет равна a2b1c5a3. Если длина не изменилась, то возвращать исходную строку
"""


def zip_string(s: str) -> str:
    prev = s[0]
    char_count = 0
    payload = []
    for i, char in enumerate(s):
        if char == prev:
            char_count += 1
        else:
            payload.append(prev)
            payload.append(str(char_count))
            prev = char
            char_count = 1

        if i+1 == len(s):
            payload.append(char)
            payload.append(str(char_count))
            
    return "".join(payload) if len(payload) < len(s) else s


print(zip_string("aabcccccaaa"))
print(zip_string("aa"))
