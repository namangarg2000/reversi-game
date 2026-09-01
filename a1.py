# DO NOT modify or add any import statements
from support import *

# Name:Naman Garg
# Student Number: 50188284 
# Favorite Boardgame: Ludo
# -----------------------------------------------------------------------------

# Define your classes and functions here

#Task 1
def get_board_size(board: list[list[str]]) -> int:
    return len(board)

#Task 2
def count_pieces(board: list[list[str]]) -> tuple[int, int]:
    player1 = 0
    player2 = 0
    for row in board:
        for piece in row:
            if piece == PLAYER_1:
                player1+=1
            elif piece == PLAYER_2:
                player2+=1 
    return (player1, player2)

#Task 3
def create_initial_board(size: int) -> list[list[str]]:
    board = []

    for i in range(0,size):
        board_row = []
        for i in range(0, size):
            board_row.append(EMPTY)
        board.append(board_row)

    put_initial_pieces(board) #function from support file

    return board

#Task 4
def display(board: list[list[str]]) -> None:
    print(' ', end='')
    for i in range(0,get_board_size(board)):
        print(f' {i+1}', end='')
    print()

    for i in range(0, get_board_size(board)):
        print(i+1, end=' ')
        for j in range(0, get_board_size(board)):
            print(board[i][j], end=' ')
        print()

#Task 5
def show_outcome(board: list[list[str]]) -> None:
    x, o = count_pieces(board) 
    display(board)
    print('--------------------')
    print(f'Player 1 (X): {x} pieces')
    print(f'Player 2 (O): {o} pieces')
    if x > o:
        print(PLAYER1_WIN_MESSAGE)
    elif x < o:
        print(PLAYER2_WIN_MESSAGE)
    else:
        print(DRAW_MESSAGE)

#Task 6
def is_valid(command: str, board: list[list[str]]) -> bool:
    pass

def play_game() -> None:
    pass

# if __name__ == "__main__":
#     play_game()


board = create_initial_board(6)
board[0][0] = 'O'
show_outcome(board)