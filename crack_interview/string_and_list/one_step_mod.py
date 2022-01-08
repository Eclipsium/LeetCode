"""
Напишите функцию, которая проверяет, находится ли две строки на расстоянии одной (нуля)
модификации (Вставка символа, удаление символа, замена символа)
pale, ple -> True
pales, pale -> True
pale, bale -> True
pale, bake -> false
"""


def check_append(s1: str, s2: str) -> bool:
    if len(s1) - len(s2) > 1:
        return False

    append_count = 0
    # итерируемся по меньшему
    for i in range(len(s2)):
        if s1[i] != s2[i]:
            s1 = s1[:i] + s1[i + 1:]  # Вырезаем символ
            append_count += 1

        if append_count > 1:
            return False
    return True


def check_replace(s1: str, s2: str) -> bool:
    replace_count = 0

    for i in range(len(s1)):
        if replace_count > 1:
            return False
        if s1[i] != s2[i]:
            replace_count += 1

    return True


def check_changes(s1: str, s2: str) -> bool:
    return check_append(s1, s2) if len(s1) > len(s2) else check_append(s2, s1)


def compare_string(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return check_changes(s1, s2)

    return check_replace(s1, s2)


assert compare_string("pela", "ple") is False
assert compare_string("pales", "pale") is True
assert compare_string("pale", "bale") is True
assert compare_string("pale", "bake") is False
