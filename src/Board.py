# Exception classes
class Error(Exception):
    pass


class CellIsFilled(Error):
    pass


class InvalidInput(Error):
    pass


class GameBoard:
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

    def isBoardFull(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] is None:
                    return False
        return True

    def evaluationFunction(self):
        # Check for row and columns win
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2]:
                if self.board[i][0] == 'X':
                    return 10
                elif self.board[i][0] == 'O':
                    return -10
            if self.board[0][i] == self.board[1][i] == self.board[2][i]:
                if self.board[0][i] == 'X':
                    return 10
                elif self.board[0][i] == 'O':
                    return -10
        # Check for diagonal win
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            if self.board[0][0] == 'X':
                return 10
            elif self.board[0][0] == 'O':
                return -10
        if self.board[2][0] == self.board[1][1] == self.board[0][2]:
            if self.board[2][0] == 'X':
                return 10
            elif self.board[2][0] == 'O':
                return -10
        # If neither of players win, return 0
        return 0


def minimax(GameBoard, alpha, beta, isMax):
    if GameBoard.isBoardFull():
        return GameBoard.evaluationFunction()
    if isMax:  # If the current player is the maximizer
        best_value = -1000  # Initialize best value to -1000 as it is symbolizes -INFINITY
        for i in range(3):
            for j in range(3):
                if GameBoard.board[i][j] is None:
                    GameBoard.board[i][j] = 'X'
                    best = max(best, minimax(
                        GameBoard, alpha, beta, False))
                    GameBoard.board[i][j] = None
                    alpha = max(alpha, best)
                    if beta <= alpha:
                        break
        return best
    else:  # If the current player is the minimizer
        best_value = 1000  # Initialize best value to 1000 as it is symbolizes +INFINITY
        for i in range(3):
            for j in range(3):
                if GameBoard.board[i][j] is None:
                    GameBoard.board[i][j] = 'O'
                    best = min(best, minimax(
                        GameBoard, alpha, beta, True))
                    GameBoard.board[i][j] = None
                    beta = min(beta, best)
                    if beta <= alpha:
                        break
        return best
