from Board import *


def main():
    print("Tic Tac Toe Game using Minimax Algorithm with Alpha-Beta Pruning")
    print("Created by: Gede Prasidha Bhawarnawa (IF'20 - 13520004)\n")
    while True:
        print("Who will play the first move? (X/O)")
        print("1. Player as 'X'")
        print("2. Computer as 'O'")
        try:
            player_choice = int(input("Input your choice here: "))
            if player_choice not in [1, 2]:
                raise InvalidInput
            player_first = True if player_choice == 1 else False
            break
        except InvalidInput:
            print("Invalid input. Try again\n")
        except ValueError:
            print("Invalid input, only accepting integers. Try again\n")
    game_board = GameBoard()


main()
