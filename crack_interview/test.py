# # Sample Input ["eat", "tea", "tan", "ate", "nat", "bat"]
# # Sample Output [ ["ate", "eat", "tea"], ["nat", "tan"], ["bat"] ]
# # Т.е. сгруппировать слова по "общим буквам".
# from collections import Counter
# from typing import List
#
# _input = ["eat", "tea", "tan", "ate", "nat", "bat"]
#
#
# def compare_with_char(data: List[str]):
#     _counter_list = []
#
#     for string in data:
#         temp_counter = Counter(string)
#         if temp_counter not in _counter_list:
#             _counter_list.append(string)
#         else:
#             _counter_list[]
#             _counter_list.append(string)
#
#
#
#     return _counter_list
#
#
# payload = compare_with_char(_input)
# print(payload)
#
#
# # 1 найти первые n простых чисел
# # 1.1 оценить сложность алгоритма
#
# def is_primary(digit: int):
#     if digit / 2 = 0 and digit != 2:
#         return False
#
#
# for i in range(2, digit + 1):
#     if i = 1:
#         continue:
#     if i != digit and digit / i == 0:
#         return False
#
#     return True
#
#
#     def get_primary_digit(n: int):
#         answer = []
#
#
#     digit = 2
#     count = 0
#     while count != n:
#         if is_primary(digit):
#     answer.append(digit)
#     count += 1
#     digit += 1
#
#     return answer
#
#     # 2 Несортированный список обьектов Студент, у которого есть поле Фамилия.
#     # Поставить всех Ивановых на первое место
#
#     sorted(a, secret_key=lambda x: '' if x['name'] == 'Иванов' else x['name'])
#
#     # Sample Input ["eat", "tea", "tan", "ate", "nat", "bat"]
#     # Sample Output [ ["ate", "eat", "tea"], ["nat", "tan"], ["bat"] ]
#     # Т.е. сгруппировать слова по "общим буквам".
#
#     from future import Counter