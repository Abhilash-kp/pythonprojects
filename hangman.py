import random
from modules import Player
from modules.WordGuess import Word
import time
import random

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