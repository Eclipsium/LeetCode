'''
Реализуйте алгоритм, определяющий, все ли символы в строке встречаются один раз. А
если запрещенно пользоваться доп структур данных?
'''


class CheckString:
    _string: str

    def __init__(self, _string: str):
        if not isinstance(_string, str):
            try:
                self._string == str(_string).lower()
            except AttributeError:
                raise AttributeError(f'Невозможно привести {_string} к строке')
        else:
            self._string = _string.lower()

    def check_easy(self):
        return len(self._string) == len(set(self._string))

    def check_without_set(self):
        counter = {}
        for char in self._string:
            if counter.get(char):
                return False
            else:
                counter[char] = 1

        return True


check_string = []

check_string.append(CheckString('asdf'))  # True
check_string.append(CheckString(''))  # True
check_string.append(CheckString('asdfa'))  # False
check_string.append(CheckString('1234'))  # True
check_string.append(CheckString('12341'))  # False
check_string.append(CheckString('20.0'))  # False
check_string.append(CheckString('AsdAs'))  # False
check_string.append(CheckString('zxcasdqwe'))  # True
# check_string.append(CheckString(['123']))  # raise

for string in check_string:
    print(string.check_easy())
    print(string.check_without_set())
