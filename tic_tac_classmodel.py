import random


class Player():

    def __init__(self, name):
        self.name = name
        self.marker = None

    @staticmethod
    def go_first():
        if random.randint(0, 1) == 0:
            return True
        else:
            return False

    def select_marker(self):
        if self.name == player1.name:
            print("{} will play first".format(player1.name))
            inp = input("{} please select a Marker (X or 0) : ".format(player1.name))
            while inp.upper() not in ['X', 'O']:
                inp = input("{} Please select one of valid option 'X' or 'O' : ".format(player1.name))

            if inp.upper() == "X":
                return 'X', 'O'
            else:
                return 'O', 'X'

        else:
            print("{} will play first".format(player2.name))
            inp = input("{} please select a Marker (X or 0) : ".format(player2.name))
            while inp.upper() not in ['X', 'O']:
                inp = input("{} Please select one of valid option 'X' or 'O' : ".format(player1.name))

            if inp.upper() == "X":
                return 'O', 'X'
            else:
                return 'X', 'O'

    def enter_value(self, val):
        while (not tic_board.space_check(val)) and (0 < val < 10):
            val = int(input("The entered position is already occupied please select a different vacant position :"))
        tic_board.board[val] = self.marker


class Board(list):

    def __init__(self):
        self.board = [" "] * 10

    def __getitem__(self, item):
        list.__getitem__(self, item)

    def __setitem__(self, key, value):
        list.__setitem__(self, key, value)

    def display_board(self):
        print()
        print()
        print(self.board[7] + " " "|" + self.board[8] + " " + "|" + self.board[9])
        print(" " + "-" + " " + "-" + " " + "-")
        print(self.board[4] + " " "|" + self.board[5] + " " + "|" + self.board[6])
        print(" " + "-" + " " + "-" + " " + "-")
        print(self.board[1] + " " "|" + self.board[2] + " " + "|" + self.board[3])
        print()
        print()

    def space_check(self, val):
        if self.board[val] == " ":
            return True
        else:
            return False

    def full_board_check(self):
        for x in range(10):
            if self.space_check(x):
                return True
        return False

    def win_check(self, mark):

        return ((self.board[7] == mark and self.board[8] == mark and self.board[9] == mark) or  # across the top
                (self.board[4] == mark and self.board[5] == mark and self.board[6] == mark) or  # across the middle
                (self.board[1] == mark and self.board[2] == mark and self.board[3] == mark) or  # across the bottom
                (self.board[7] == mark and self.board[4] == mark and self.board[1] == mark) or  # down the middle
                (self.board[8] == mark and self.board[5] == mark and self.board[2] == mark) or  # down the middle
                (self.board[9] == mark and self.board[6] == mark and self.board[3] == mark) or  # down the right side
                (self.board[7] == mark and self.board[5] == mark and self.board[3] == mark) or  # diagonal
                (self.board[9] == mark and self.board[5] == mark and self.board[1] == mark))  # diagonal


print("Welcome to Tic-Tac-Toe Game")
tic_board = Board()

player1 = Player(input("Player1 please enter your name : "))
player2 = Player(input("Player2 please enter your name : "))

if player1.go_first():
    player1.marker, player2.marker = player1.select_marker()
    turn = player1
else:
    player1.marker, player2.marker = player2.select_marker()
    turn = player2

tic_board.display_board()

while True:
    if turn == player1:
        while True:
            try:
                val = int(input("{} please enter a position between 1 and 9 : ".format(player1.name)))
                while val not in range(1, 10):
                    val = int(input("{} Please enter a valid position between 1 and 9 : ".format(player1.name)))
                break
            except Exception:
                pass

 #       while val not in range(1, 10) :
 #           while True:
 #               try:
 #                   val = int(input("{} Please enter a valid position between 1 and 9 : ".format(player1.name)))
  #              except Exception:
  #                  pass

        player1.enter_value(val)
        tic_board.display_board()
        if tic_board.win_check(player1.marker):
            print("Congratulations {} has won".format(player1.name))
            break
        if not tic_board.full_board_check():
            print("The Game is a Draw")
            break

        turn = player2

    if turn == player2:
        while True:
            try:
                val = int(input("{} please enter a position between 1 and 9 : ".format(player2.name)))
                while val not in range(1, 10):
                    val = int(input("{} Please enter a valid position between 1 and 9 : ".format(player2.name)))
                break
            except Exception:
                pass
        #val = int(input("{} please enter a position : ".format(player2.name)))
        #while val not in range(1, 10):
        #    val = int(input("{} Please enter a valid position between 1 and 9 : ".format(player2.name)))

        player2.enter_value(val)
        tic_board.display_board()
        if tic_board.win_check(player2.marker):
            print("Congratulations {} has won".format(player2.name))
            break
        if not tic_board.full_board_check():
            print("The Game is a Draw")
            break

        turn = player1


print("Thanks For Playing")

















