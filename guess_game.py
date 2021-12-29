import random
from modules import Player
import time


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


word = Word()
user = Player.Player(input("Please enter your name : "))
print()
user.intro()
time.sleep(4)
print("The below is the word to be guessed ")
word.generate_word()
time.sleep(3)
print()

if len(word.word) > 5:
    print("{} you will have two guesses to guess this word ".format(user.name))
    print()
    user.wordguess(word, 1)
    print()
    user.wordguess(word, 2)
    print()
else:
    print("{} you will have one guess to guess this word".format(user.name))
    user.wordguess(word, 1)
    print()

final_guess = input("{} you have utilized your available guesses kindly enter the complete word : ".format(user.name))
print()
if final_guess.lower() == word.word.lower():
    print()
    print("Congratulations {} you have guessed it correctly.".format(user.name))
    print()
    print("Hidden Word - {} ".format(word.word))

else:
    print()
    print("The entered word is not the same as the hidden word, Better luck next time")
    print()
    print("Hidden Word - {} ".format(word.word))
















