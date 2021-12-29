import random

def board(board):
    print()
    print()
    print(board[7] + " " "|" + board[8] + " " + "|" + board[9])
    print(" " + "-" + " " + "-" + " " + "-")
    print(board[4] + " " "|" + board[5] + " " + "|" + board[6])
    print(" " + "-" + " " + "-" + " " + "-")
    print(board[1] + " " "|" + board[2] + " " + "|" + board[3])
    print()

#board(['#','1','2','3','4','5','6','7','8','9'])

def play_first():
    print("-----------------------------------------------")
    print("    WELCOME TO THE GAME     ")
    print("-----------------------------------------------")
    print()
    rn = random.randint(0,1)
    if rn == 0:
        print("Player 1 will go first.")
        print()
        return "Player1"
    else:
        print("Player 2 will go first.")
        print()
        return "Player2"

def select_marker(Player):
    if Player == "Player1":
        player1_marker = input("Player 1 Select your Marker: (X or O)")
        if player1_marker.upper() == "X":
            return 'X', 'O'
        else:
            return 'O', 'X'
    else:
        player2_marker = input("Player 2 Select your Marker: (X or O)")
        if player2_marker.upper() == "X":
            return 'O', 'X'
        else:
            return 'X', 'O'


#Turn = play_first()
#Player1_marker, Player2_marker = select_marker(Turn)

def intro():
    print("Welcome to Tic-Tac Toe Game!")
    res = input("Do you want to play now? (Y/N) ")
    tic_board = [" "] * 10
    if res.lower() == "y":
        game_on = True
    else:
        game_on = False
        return game_on, "#", "#", "#", tic_board

    if game_on == True:
        Turn = play_first()
        player1_marker, player2_marker = select_marker(Turn)
        # play(Player1_marker, Player2_marker,Turn)
        return game_on, player1_marker, player2_marker, Turn, tic_board

def check_space(board, val):
    if board[val] == " ":
        return True
    else:
        return False

def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal


def board_check(board):
    for x in range(1,10):
        if check_space(board,x):
            return True
    return False


while True:
    game_on, Player1_marker, Player2_marker, Turn, tic_board = intro()
    # board(tic_board)

    while game_on == True:
        board(tic_board)
        if Turn == "Player1":
            print()
            val = int(input("Player1 enter the position (1-9) where you want the marker : "))
            print()
            while val not in range(1, 10):
                val = int(input("Kindly enter a value between 1 and 9 : "))
                print()
            while not check_space(tic_board, val):
                val = int(input("The position " + str(val) + " is already occupied, select a different position: "))
                print()

            tic_board[val] = Player1_marker
            board(tic_board)
            if win_check(tic_board, Player1_marker):
                print()
                print("-------------------------------------")
                print(" Congratulations Player1 won ")
                print("-------------------------------------")

                board(tic_board)
                game_on = False
                break

            if not board_check(tic_board):
                print()
                print("-------------------------------------")
                print("The Game is a Draw")
                print("-------------------------------------")
                print()
                board(tic_board)
                game_on = False
                break

            Turn = "Player2"

        if Turn == "Player2":
            print()
            val = int(input("Player2 enter the position (1-9) where you want the marker : "))
            print()
            while val not in range(1, 10):
                val = int(input("Kindly enter a value between 1 and 9 : "))
                print()
            while not check_space(tic_board, val):
                val = int(input("The position " + str(val) + " is already occupied, select a different position: "))
                print()

            tic_board[val] = Player2_marker
            board(tic_board)
            if win_check(tic_board, Player2_marker):
                print()
                print("-------------------------------------")
                print(" Congratulations Player2 won ")
                print("-------------------------------------")
                board(tic_board)
                game_on = False
                break

            if not board_check(tic_board):
                print()
                print("-------------------------------------")
                print("The Game is a Draw")
                print("-------------------------------------")
                game_on = False
                board(tic_board)
                break

            Turn = "Player1"






































