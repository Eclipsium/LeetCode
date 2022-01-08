"""
Напишите функцию, которая проверяет, является ли строка перестановкой палиндрома
Например Tact Coa является перестановкой taco cat
"""
from collections import Counter


def check_even_palindrome(s: str) -> bool:
    counter = Counter(s)
    for count in counter.values():
        if count % 2 != 0:
            return False

    return True


def check_odd_palindrome(s: str) -> bool:
    counter = Counter(s)
    center_char_count = 0

    for count in counter.values():
        if count % 2 != 0:
            center_char_count += 1
        if center_char_count > 1:
            return False
    return True


def check_palindrome(s: str) -> bool:
    # Убираем пробелы и приводим в нижний регистр
    s = s.replace(" ", "").lower()
    if len(s) % 2 == 0:
        return check_even_palindrome(s)
    return check_odd_palindrome(s)


print(check_palindrome("Tact Coa"))
