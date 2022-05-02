import random
import re
from os.path import exists


class VernamCrypto:
    raw_text_filename: str = "raw_text.txt"
    crypto_text_filename: str = "crypto_text.txt"
    key_filename: str = "key.txt"

    raw_text: str
    crypto_text: str
    secret_key: str

    int_to_char_rus: dict[int: str] = {}  # {0: "A", 1: "B"...}
    char_to_int_rus: dict[str: int] = {}  # {"A": 0, "B": 1...}

    def __init__(self):
        """
        Инизиализируем класс
        Заполняем данные из файлов и технические поля
        """
        self.raw_text = self.__get_file_data(self.raw_text_filename)
        self.crypto_text = self.__get_file_data(self.crypto_text_filename)
        self.secret_key = self.__get_file_data(self.key_filename)

        for i in range(32):
            self.int_to_char_rus[i] = chr(ord('А') + i)
            self.char_to_int_rus[chr(ord('А') + i)] = i

    def __generate_random_key(self, key_len: int):
        self.secret_key = "".join(
            [
                self.int_to_char_rus[random.randint(0, 31)] for _ in range(key_len)
            ]
        )
        print(f'Новый сгенерированный ключ: \n{self.secret_key}')
        self.__save_to_file(filename=self.key_filename, data=self.secret_key)

    def __get_file_data(self, filename: str):
        # Создаем файл если он не найден
        if not exists(filename):
            with open(filename, mode='a'):
                return ""

        with open(filename, 'r', encoding="utf-8") as file:
            # Забираем 1 строку текста, переводим его в верхний регист и убираем пробелы
            text = file.readline().upper().replace(" ", "")
            # Проверяем регуляркой, что файл содержит только заглавные русские символы
            if not bool(re.match('^[А-Я]+$', text)):
                raise ValueError(f"Файл {filename} содержит лишние символы!")
            return text

    def __save_to_file(self, filename: str, data: str):
        with open(filename, "w", encoding="utf-8") as file:
            file.write(data)

    def encrypt(self, text: str = None):
        if text:
            self.raw_text = text
        if len(self.secret_key) < len(self.raw_text):
            print("Длина ключа не может быть меньше длины сообщения. Генерируем новый")
            self.__generate_random_key(key_len=len(self.raw_text))

        print("Чистый текст")
        print(self.raw_text)

        crypto_text = []
        for index, char in enumerate(self.raw_text):
            # Переводим символ в позицию русского алфавита
            # делим по остатку на 1040 (символ русской А в юникоде) и получаем
            # позицию в русском алфавите секретного ключа.
            # Делим по остатку на 32, чтоб получить число, русского алфавита,
            # если сумма получилась > 32
            symbol_utf_index = (self.char_to_int_rus[char]
                                + ord(self.secret_key[index]) % ord('А')) % 32
            # Прибавляем позицию русской A в юникоде. Можно прибавить 1040
            symbol = chr(symbol_utf_index + ord('А'))
            crypto_text.append(symbol)

        self.crypto_text = ''.join(crypto_text)
        print("\nЗашифрованный текст")
        print(self.crypto_text)

        self.__save_to_file(self.crypto_text_filename, data=self.crypto_text)
        return self.crypto_text

    def decrypt(self, text: str = None):
        if text:
            self.crypto_text = text

        if len(self.secret_key) < len(self.crypto_text):
            raise ValueError("Длина ключа не может быть меньше длины зашифрованного "
                             "текста")
        raw_text = []
        for index, char in enumerate(self.crypto_text):
            symbol_utf_index = (self.char_to_int_rus[char] - ord(
                self.secret_key[index]) % 1040) % 32
            symbol = chr(symbol_utf_index + ord('А'))

            raw_text.append(symbol)

        self.raw_text = ''.join(raw_text)
        print("Расшифрованный текст")
        print(self.raw_text)

        self.__save_to_file(self.raw_text_filename, data=self.raw_text)
        return self.raw_text


varnam = VernamCrypto()
varnam.encrypt()
varnam.decrypt()
