"""Реализуйте метод, заменяющий пробелы в строке на %20
"""


def replace_to_20(s: str) -> str:
    return s.strip().replace(" ", "%20")


def replace_without_lib(s: str) -> str:
    payload = []
    index = 0
    for i, char in enumerate(s.strip()):
        if char == " ":

            payload.append("%20")
        else:
            payload.append(char)
    return "".join(payload)


string = '  Hello  from python  '
assert replace_to_20(string) == replace_without_lib(string)
