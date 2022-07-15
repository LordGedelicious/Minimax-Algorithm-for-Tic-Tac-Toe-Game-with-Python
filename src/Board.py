from Minimax import *

# Exception classes


class Error(Exception):
    pass


class CellIsFilled(Error):
    pass


class InvalidInput(Error):
    pass


class Board:
    def __init__(self):
        self.board = [[None for i in range(3)] for j in range(3)]

    def printBoard(self):
        for i in range(3):
            for j in range(3):
                print(self.board[i][j], end=" ")
            print()
        print()

    def addObjectToBoard(self, object, position):
        x_coordinate = position % 3
        y_coordinate = position - x_coordinate * 3
        try:
            if self.board[x_coordinate][y_coordinate] is not None:
                raise CellIsFilled
            self.board[x_coordinate][y_coordinate] = object
        except CellIsFilled:
            print("Cell is already filled. Try again")
            return False
        except IndexError:
            print("Invalid input. Try again")
            return False
        return True
