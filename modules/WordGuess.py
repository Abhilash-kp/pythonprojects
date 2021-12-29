import random

class Word():
    list1 = []
    word_list = ['apple', 'october', 'autumn', 'giraffe', 'pineapple', 'washington', 'neighbour', 'place', 'table']

    def __init__(self):
        self.word = Word.choose_word()
        self.displayed_word = ''
        self.list1[:0] = self.word

    @classmethod
    def choose_word(cls):
        return random.choice(cls.word_list)

    def generate_word(self):
        if len(self.word) > 7:
            self.display_word_initial(2)
        else:
            self.display_word_initial(1)

    def display_word_initial(self, num):
        self.displayed_word = ["  _  "] * len(self.word)
        for i in range(num):
            lst = list(range(len(self.word)))
            ind = random.choice(lst)
            self.displayed_word[ind] = " " + self.word[ind] + " "
            lst.remove(ind)
        print()
        print(self.displayed_word)