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
        for x in range(1, 10):
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