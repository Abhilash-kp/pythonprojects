import random

def ask_game():
    print("Hello!")
    print("-----------Welcome to the Game!-------------------")
    Response = input("DO you want to play now? (Y/N)")
    if Response == 'y':
        play_game()
    else:
       ask_game()

def play_game():
    guess_word = random.choice(available_words).lower()
    display_word = ''
    list1 = []
    list1[:0] = guess_word
    #print(list1)
    if len(guess_word) > 7:
        displayed_word = ["  _  "] * len(guess_word)
        lst = list(range(len(guess_word)))
        for n in range(2):
            id = random.choice(lst)
            displayed_word[id] = " " + guess_word[id] + " "
            lst.remove(id)

    else:
        displayed_word = ["  _  "] * len(guess_word)
        lst = list(range(len(guess_word)))
        id = random.choice(lst)
        displayed_word[id] = " " + guess_word[id] + " "

    #print("Displayed word :", displayed_word)

    display_word = display_word.join(displayed_word)

    #print(type(display_word))
    #print(display_word[:3])

    print(display_word)
    print()

    print('-------------------------------------------------------------------------------')
    response2 = input("The above is the word to be guessed, Do you want to continue? (Y/N)")
    print()
    if response2 == 'y':
        lets_play(display_word, displayed_word, list1, guess_word)
    else:
        ask_game()

def lets_play(wrd_dsp, wrd_dspled, lst1,guess_word):
    print("Great! Lets Play.")
    if len(guess_word) > 7:
        print("---------------------------------------------------")
        print("You will have two guesses available with you ")
        for n in range(2):
            guess = input("Please enter your Guess {} : ".format(n+1))
            print('Your Guess is  {} '.format(guess))
            if guess in lst1:
                wrd_dsp = ""
                ind = lst1.index(guess)
                lst1[ind] = '*'
                wrd_dspled[ind] = " " + guess + " "
                #print(wrd_dspled)
                print(wrd_dsp)
                wrd_dsp = wrd_dsp.join(wrd_dspled)
                # wrd_dsp1 = wrd_dsp[:ind] + guess + wrd_dsp[ind + 1:]
                print("---------------------------------------------------")
                print("The letter you guessed is present in the word")
                print()
                print("The word now becomes :  ", wrd_dsp)
                print("--------------------------------------------------------------------------")
                print("--------------------------------------------------------------------------")
                if n != 1:
                    ress = input("You have one more guess available ,Do you want to use that ? (Y/N)")
                    if ress.lower() == 'y':
                        continue
                    else:
                        print("Since you are not using the available guess, Kindly enter the complete word: ")
                        print()
                        ip = input("Enter the complete word : ")
                        if ip.lower() == guess_word.lower():
                            print("--------------------------------------------------------------")
                            print("-----Congratulations! You have guessed the correct word-----")
                            print()
                            print()
                            re = input("Do you want to play again? (Y/N)")
                            if re.lower() == 'y':
                                play_game()
                            else:
                                ask_game()
                        else:

                            print("---------------------------------------------------------------------------")
                            print("Unfortunately this is an incorrect word. The correct word is : ", guess_word)
                            print()
                            print("Thanks For Playing!")
                            print()
                            print("------------------------------------------------------------------------------")
                            re = input("Do you want to play again? (Y/N)")
                            if re.lower() == 'y':
                                 play_game()
                            else:
                                 ask_game()


                else:
                    print("You have used both your guesses. Kindly input the complete word:  ")
                    ip = input("Enter the complete word : ")
                    if ip.lower() == guess_word.lower():
                        print()
                        print('--------------------------------------------------------------')
                        print("Congratulations! You have guessed the correct word")
                        print()
                        re = input("Do you want to play again? (Y/N)")
                        if re.lower() == 'y':
                            play_game()
                        else:
                            ask_game()
                    else:
                        print("Unfortunately this is an incorrect word. The correct word is : ", guess_word)
                        print("Thanks For Playing!")
                        re = input("Do you want to play again? (Y/N)")
                        if re.lower() == 'y':
                            play_game()
                        else:
                            ask_game()

            else:
                print("The letter you guessed is not present in the word: ")
                if n != 1:
                    print("Now Kindly enter the second Guess:")
                    continue
                else:
                    print("--------------------------------------------------------------------------")
                    print("--------------------------------------------------------------------------")

                    print("You have used your available guess, now you need to type down the correct word")
                    print(wrd_dsp)
                    ip = input("Enter the complete word : ")
                    if ip.lower() == guess_word.lower():
                        print("Congratulations! You have guessed the correct word")
                        re = input("Do you want to play again? (Y/N)")
                        if re.lower() == 'y':
                            play_game()
                        else:
                            ask_game()
                    else:
                        print("Unfortunately this is an incorrect word. The correct word is : ", guess_word)
                        print("Thanks For Playing!")
                        re = input("Do you want to play again? (Y/N)")
                        if re.lower() == 'y':
                            play_game()
                        else:
                            ask_game()

    else:
        print("You will have a single guess available with you")
        guess = 10
        while (type(guess) != type("b")):
            guess = input("Please enter your Guess: ")
        print('Your Guess is {}'.format(guess))

        if guess in lst1:
            wrd_dsp = ""
            ind = lst1.index(guess)
            lst1[ind] = '*'
            wrd_dspled[ind] = " " + guess + " "
            print(wrd_dspled)
            # print(wrd_dsp)
            wrd_dsp = wrd_dsp.join(wrd_dspled)
            # wrd_dsp1 = wrd_dsp[:ind] + guess + wrd_dsp[ind + 1:]
            print("The letter you guessed is present in the word")
            print("The word now becomes : ", wrd_dsp)
            print("--------------------------------------------------------------------------")
            print("--------------------------------------------------------------------------")

            print("You have used your available guess, now you need to type down the correct word")
            ip = input("Enter the complete word : ")
            if ip.lower() == guess_word.lower():
                print("Congratulations! You have guessed the correct word")
                re = input("Do you want to play again? (Y/N)")
                if re.lower() == 'y':
                    play_game()
                else:
                    ask_game()
            else:
                print("Unfortunately this is an incorrect word. The correct word is : ", guess_word)
                print("Thanks For Playing!")
                re = input("Do you want to play again? (Y/N)")
                if re.lower() == 'y':
                    play_game()
                else:
                    ask_game()


        else:
            print("The letter you guessed is not present in the word: ")
            #print("You don't have any more guesses left. The correct word is : ", guess_word)
            print("You have used your available guess, now you need to type down the correct word")
            ip = input("Enter the complete word : ")
            if ip.lower() == guess_word.lower():
                print("Congratulations! You have guessed the correct word")
                re = input("Do you want to play again? (Y/N)")
                if re.lower() == 'y':
                    play_game()
                else:
                    ask_game()
            else:
                print("Unfortunately this is an incorrect word. The correct word is : ", guess_word)
                print("Thanks For Playing!")
                re = input("Do you want to play again? (Y/N)")
                if re.lower() == 'y':
                    play_game()
                else:
                    ask_game()

            print("Thanks for playing")
            ask_game()



available_words = ['Parent', 'Aeroplane', 'Motorcycle','Elephant','Soil','Lion',"Alphabet",'Solar','Digitization',"Globalisation","Nutrition"]
#guess_word = random.choice(available_words)
ask_game()

"""import random

def ask_game():
    print("Hello!")
    print("Welcome to the Game!")
    Response = input("DO you want to play now? (Y/N)")
    if Response == 'y':
        print("We will play")
        play_game()
    else:
       ask_game()

def play_game():
    guess_word = random.choice(available_words).lower()
    display_word = ''
    list1 = []
    list1[:0] = guess_word
    print(list1)
    if len(guess_word) > 5:
        displayed_word = ["  _  "] * len(guess_word)
        lst = list(range(len(guess_word)))
        for n in range(2):
            id = random.choice(lst)
            displayed_word[id] = " " + guess_word[id] + " "
            lst.remove(id)

    else:
        displayed_word = ["  _  "] * len(guess_word)
        lst = list(range(len(guess_word)))
        id = random.choice(lst)
        displayed_word[id] = " " + guess_word[id] + " "

    print("Displayed word :", displayed_word)

    display_word = display_word.join(displayed_word)

    print(type(display_word))
    print(display_word[:3])

    print(display_word)
    print()
    response2 = input("The above is the word to be guessed, DO you want to continue? (Y/N)")
    if response2 == 'y':
        lets_play(display_word, displayed_word, list1, guess_word)
    else:
        ask_game()

def lets_play(wrd_dsp, wrd_dspled, lst1,guess_word):
    print("Great! Lets Play.")
    print("You will have a single guess available with you")
    guess = 10
    while ( type(guess) != type("b")):
        guess = input("Please enter your Guess: ")
    print('Your Guess is {}'.format(guess))

    if guess in lst1:
        wrd_dsp = ""
        ind = lst1.index(guess)
        lst1[ind] = '*'
        wrd_dspled[ind] = " " + guess + " "
        print(wrd_dspled)
        #print(wrd_dsp)
        wrd_dsp = wrd_dsp.join(wrd_dspled)
        #wrd_dsp1 = wrd_dsp[:ind] + guess + wrd_dsp[ind + 1:]
        print("The letter you guessed is present in the word")
        print("The word now becomes : ", wrd_dsp)
        print("--------------------------------------------------------------------------")
        print("--------------------------------------------------------------------------")

        print("You have used your available guess, now you need to type down the correct word")
        ip = input("Enter the complete word : ")
        if ip.lower() == guess_word.lower():
            print("Congratulations! You have guessed the correct word")
            re = input("Do you want to play again? (Y/N)")
            if re.lower() == 'y':
                play_game()
            else:
                ask_game()
        else:
            print("Unfortunately this is an incorrect word. The correct word is : ", guess_word)
            print("Thanks For Playing!")
            re = input("Do you want to play again? (Y/N)")
            if re.lower() == 'y':
                play_game()
            else:
                ask_game()


    else:
        print("The letter you guessed is not present in the word: ")
        print("You don't have any more guesses left. The correct word is : ", guess_word)
        print("Thanks for playing")
        ask_game()

available_words = ['Parent', 'Aeroplane', 'Motorcycle','Elephant','Soil','Lion']
guess_word = random.choice(available_words)
ask_game() """












