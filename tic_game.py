from modules.Player import Player
from modules.Board import Board

print("Welcome to Tic-Tac-Toe Game")
tic_board = Board()

player1 = Player(input("Player1 please enter your name : "))
player2 = Player(input("Player2 please enter your name : "))

if player1.go_first():
    player1.marker, player2.marker = player1.select_marker(player1.name, player2.name)
    turn = player1
else:
    player1.marker, player2.marker = player2.select_marker(player1.name, player2.name)
    turn = player2

tic_board.display_board()

while True:
    if turn == player1:
        player1.enter_value(tic_board)
        tic_board.display_board()
        if tic_board.win_check(player1.marker):
            print("Congratulations {} has won".format(player1.name))
            break
        if not tic_board.full_board_check():
            print("The Game is a Draw")
            break

        turn = player2

    if turn == player2:
        player2.enter_value(tic_board)
        tic_board.display_board()
        if tic_board.win_check(player2.marker):
            print("Congratulations {} has won".format(player2.name))
            break
        if not tic_board.full_board_check():
            print("The Game is a Draw")
            break

        turn = player1

print("Thanks For Playing")