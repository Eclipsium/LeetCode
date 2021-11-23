"""
Для двух строк, напишите метод, определяющий, является ли одна строка перестановкой
другой
"""
from collections import Counter


class CompareString:
    _first_str: str
    _second_str: str

    def __init__(self, first: str, second: str):
        self._first_str = first
        self._second_str = second

    def compare(self):
        if len(self._first_str) != len(self._second_str):
            return False

        return Counter(self._first_str) == Counter(self._second_str)


a = CompareString('asd asd ', 'dsa dsa ')
print(a.compare())
