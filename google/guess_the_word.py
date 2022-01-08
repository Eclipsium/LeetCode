"""
https://leetcode.com/problems/guess-the-word/
Угадай слово.
Дан список слов из 6 букв, например, WEWEWE WEEWEE DUGDUN и тд до 100
Человек загадывает слово, а мы должны его угадать. После выбора слова человек говорит
количество позиций, которые входят в текуще слово.
Допустим  'D'U'N'G`E'N' - 'D'A'N'W`O'N' - 3 буквы находятся в одинаковых местах
Если слово, которого нет вхождений отдается -1
Допускается не более 10 попыток
"""
import random
import string
from typing import List


class Solution:
    def __init__(self, wordlist: List[str], master: str):
        self._wordlist = wordlist
        self._master = master
        self._attempt = 1

    def find_secret_word(self) -> None:
        print(f'Attempt #{self._attempt}')

        check_word = random.choice(self._wordlist)

        if self._attempt > 10:
            print('Fail')
            return

        count = self.compare_word(check_word, self._master)

        if count == 6:
            print(f'We do it at {self._attempt} attempt!'
                  f' Master word is {check_word}')
            return

        self.clean_up_word_list(check_word, count)

        self._attempt += 1
        print(f'{check_word} is not master\n')
        self.find_secret_word()

    def clean_up_word_list(self, check_word: str, count: int):
        temp_word_list = set(self._wordlist)
        for word in temp_word_list:
            check_count = self.compare_word(word_one=word, word_two=check_word)
            if check_count != count:
                self._wordlist.remove(word)

    def compare_word(self, word_one: str, word_two: str):
        count = 0
        for index in range(6):
            if word_one[index] == word_two[index]:
                count += 1
        return count if count else -1


gen_wordlist = [''.join(random.choice(string.ascii_lowercase)
                        for x in range(6))
                for y in range(100)]
solution = Solution(wordlist=gen_wordlist, master=random.choice(gen_wordlist)
                    )
solution.find_secret_word()
