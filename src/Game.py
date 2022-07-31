# Exception classes
from turtle import position


class Error(Exception):
    pass


class CellIsFilled(Error):
    pass


class InvalidInput(Error):
    pass


class GameBoard:
    def __init__(self):
        self.board = [['.' for i in range(3)] for j in range(3)]
        # The human player's turn (P) or the computer's turn (C)
        self.current_move = 'P'

    def printBoard(self):
        for i in range(3):
            for j in range(3):
                print("{}|".format(self.board[i][j]), end="")
            print()
        print()

    def printReferenceBoard(self):
        print("You may use the following block numbers as reference:\n")
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '.':
                    print("{}|".format(i * 3 + j), end="")
                else:
                    print("{}|".format(self.board[i][j]), end="")
            print()
        print()

    def addObjectToBoard(self, object, position):
        x_coordinate = position // 3
        y_coordinate = position - x_coordinate * 3
        print("Attempting to add {} to ({}, {})".format(
            object, x_coordinate, y_coordinate))
        try:
            if self.board[x_coordinate][y_coordinate] != '.':
                raise CellIsFilled
            self.board[x_coordinate][y_coordinate] = object
        except CellIsFilled:
            print("Cell is already filled. Try again")
            return False
        except IndexError:
            print("Invalid input. Try again")
            return False
        # except Exception:
        #     print("Something went wrong. Try again")
        #     return False
        return True

    def isBoardFull(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '.':
                    return False
        return True

    def isGameWon(self):
        # Check for row and columns win
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return self.board[0][i]
        # Check for diagonal win
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.board[0][0]
        if self.board[2][0] == self.board[1][1] == self.board[0][2]:
            return self.board[2][0]
        # If neither of players win, return 0
        return "?"

    def evaluationFunction(self, depth):
        # Check for row and columns win
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2]:
                if self.board[i][0] == 'X':
                    return 10 - depth
                elif self.board[i][0] == 'O':
                    return depth - 10
            if self.board[0][i] == self.board[1][i] == self.board[2][i]:
                if self.board[0][i] == 'X':
                    return 10 - depth
                elif self.board[0][i] == 'O':
                    return depth - 10
        # Check for diagonal win
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            if self.board[0][0] == 'X':
                return 10 - depth
            elif self.board[0][0] == 'O':
                return depth - 10
        if self.board[2][0] == self.board[1][1] == self.board[0][2]:
            if self.board[2][0] == 'X':
                return 10 - depth
            elif self.board[2][0] == 'O':
                return depth - 10
        # If neither of players win, return 0
        return 0

    def max(self, alpha, beta):
        # Initialize the maximum value to -100 which is worse than the possible worst case
        # -1 if lose, 0 if tie, 1 if tie (from the computer's perspective)
        maximum_value = -100
        # Initialize the position of x and y for best move (because one wrong move means an auto-win for the computer, also to prove that the algorithm is working)
        position_x = None
        position_y = None

        # Check the current state of the board
        if self.isBoardFull():
            if self.isGameWon() == 'X':
                return -1, 0, 0
            elif self.isGameWon() == 'O':
                return 1, 0, 0
            elif self.isGameWon() == '?':
                return 0, 0, 0

        # In the case that the board is not full, the algorithm will give the best move for the computer
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '.':  # If slot is empty
                    # Add the computer's symbol to the board. Then it will call the min function to branch out the tree and pick the best move for the computer
                    self.board[i][j] = 'O'
                    # Call the min function to branch out the tree and pick the best move for the computer
                    temp_max, temp_x, temp_y = self.min(alpha, beta)
                    if temp_max > maximum_value:
                        maximum_value = temp_max  # Update the maximum value
                        position_x = i  # Update the position of x
                        position_y = j  # Update the position of y
                    # Return the board to the initial state
                    self.board[i][j] = '.'

                    # Alpha beta pruning makes sure that the algorithm will not check branches
                    # that will not lead to a better outcome for the computer (or for the player, depending the turn)
                    # In the "max" algorithm, if the other branches are higher in value than the beta value, the algorithm will not check them

                    if maximum_value >= beta:
                        return maximum_value, position_x, position_y
                    if maximum_value > alpha:
                        alpha = maximum_value

        return maximum_value, position_x, position_y

    def min(self, alpha, beta):
        # Initialize the maximum value to 2 which is greater than the possible best case
        # -1 if lose, 0 if tie, 1 if win (from the computer's perspective)
        minimum_value = 2
        # Initialize the position of x and y for best move (because one wrong move means an auto-win for the computer, also to prove that the algorithm is working)
        position_x = None
        position_y = None

        # Check the current state of the board
        if self.isBoardFull():
            if self.isGameWon() == 'X':
                return -1, 0, 0
            elif self.isGameWon() == 'O':
                return 1, 0, 0
            elif self.isGameWon() == '?':
                return 0, 0, 0

        # In the case that the board is not full, the algorithm will give the best move for the computer
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '.':  # If slot is empty
                    # Add the computer's symbol to the board. Then it will call the min function to branch out the tree and pick the best move for the computer
                    self.board[i][j] = 'X'
                    # Call the min function to branch out the tree and pick the best move for the computer
                    temp_min, temp_x, temp_y = self.max(alpha, beta)
                    if temp_min < minimum_value:
                        minimum_value = temp_min  # Update the maximum value
                        position_x = i  # Update the position of x
                        position_y = j  # Update the position of y
                    # Return the board to the initial state
                    self.board[i][j] = '.'

                    # Alpha beta pruning makes sure that the algorithm will not check branches
                    # that will not lead to a better outcome for the computer (or for the player, depending the turn)
                    # In the "min" algorithm, if the other branches are lower than the alpha value, the algorithm will not check them
                    if minimum_value <= alpha:
                        return minimum_value, position_x, position_y
                    if minimum_value < beta:
                        beta = minimum_value

        return minimum_value, position_x, position_y

    def play_game(self):
        print("Welcome to Tic Tac Toe!")
        print("Created by Gede Prasidha Bhawarnawa")
        print("IF 2020 - 13520004")
        print("With online references, github repositories, and GeeksForGeeks.com\n")
        while True:
            if self.isBoardFull():
                if self.isGameWon() == 'X':
                    print("YOU WIN!")
                    break
                elif self.isGameWon() == 'O':
                    print("YOU LOSE!")
                    break
                elif self.isGameWon() == '?':
                    print("TIE!")
                    break
            # The player will always go first
            if self.current_move == "P":
                isTurnValid = True
                while isTurnValid:
                    minimum_value, position_x, position_y = self.min(-100, 100)
                    print("Current state of the board:\n")
                    self.printBoard()
                    print("Recommended move is at block number {}.\n".format(
                        position_x * 3 + position_y))
                    self.printReferenceBoard()
                    move = int(
                        input("Enter the block number to place your symbol (X): "))
                    if self.addObjectToBoard("X", move):
                        self.current_move = "C"
                        isTurnValid = False
                    else:
                        continue
            else:
                # The computer's turn
                maximum_value, position_x, position_y = self.max(-100, 100)
                self.addObjectToBoard("O", position_x * 3 + position_y)
                self.current_move = "P"


def main():
    game = GameBoard()
    game.play_game()


main()
