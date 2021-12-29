import random
from modules.Board import Board
from modules.WordGuess import Word


class Player():

    def __init__(self, name):
        self.name = name
        self.marker = None
        self.guess = ''

    @staticmethod
    def go_first():
        if random.randint(0, 1) == 0:
            return True
        else:
            return False

    def select_marker(self, name1, name2):
        if self.name == name1:
            print("{} will play first".format(name1))
            inp = input("{} please select a Marker (X or 0) : ".format(name1))
            while inp.upper() not in ['X', 'O']:
                inp = input("{} Please select one of valid option 'X' or 'O' : ".format(name1))

            if inp.upper() == "X":
                return 'X', 'O'
            else:
                return 'O', 'X'

        else:
            print("{} will play first".format(name2))
            inp = input("{} please select a Marker (X or 0) : ".format(name2))
            while inp.upper() not in ['X', 'O']:
                inp = input("{} Please select one of valid option 'X' or 'O' : ".format(name2))

            if inp.upper() == "X":
                return 'O', 'X'
            else:
                return 'X', 'O'

    def enter_value(self, tic_board):
        while True:
            try:
                val = int(input("{} please enter a position between 1 and 9 : ".format(self.name)))
                while (val not in list(range(1, 10))) or (not tic_board.space_check(val)):
                    val = int(input("{} the entered position may be already occupied or its not between 1 and 9: ".format(self.name)))

                break
            except Exception:
                pass
        tic_board.board[val] = self.marker


# Functionalities for word guess game

    def intro(self):
        print("Dear {} welcome to the game".format(self.name))
        print("Depending on the length of the words you will have either 1 or 2 guesses available")
        print()
        return


    def wordguess(self, words, i):
        alphabet = []
        for letter in range(97, 123):
            alphabet.append(chr(letter))

        self.guess = input("{} please enter your guess {} (any alphabet from a-z) :  ".format(self.name, i))
        print()
        while self.guess.lower() not in alphabet:
            self.guess = input("{} please enter any alphabet from a-z (guess - {}) :  ".format(self.name, i))
            print()

        print('Your Guess is  {} '.format(self.guess))
        if self.guess in words.list1:
            print("The guessed letter is present in the word. ")
            print()
            guess_ind = words.list1.index(self.guess)
            words.list1[guess_ind] = '*'
            words.displayed_word[guess_ind] = " " + self.guess + " "
            print("The word now becomes - {} ".format(words.displayed_word))
            print()

        else:
            print("The guessed letter is not present in the word.")
            print()
            print("The word remains the same - {} ".format(words.displayed_word))
            print()










