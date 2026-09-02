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
    print('   ', end='')
    for i in range(0,get_board_size(board)):
        print(f'{i+1} ', end='')
    print()

    for i in range(0, get_board_size(board)):
        print(i+1, end='  ')
        for j in range(0, get_board_size(board)):
            print(board[i][j], end=' ')
        print()
    print(SEP)

#Task 5
def show_outcome(board: list[list[str]]) -> None:
    x, o = count_pieces(board) 
    display(board)
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
    board_size_str = f'{get_board_size(board)}'

    if command in HELP_COMMAND:
        return True
    elif command in QUIT_COMMAND:
        return True
    elif len(command) == 3 and command[0] >= '1' and command[0] <=  board_size_str and command[1] == ',' and command[2] >= '1' and command[2] <= board_size_str:
        return True
    else:
        print(INVALID_COMMAND_MESSAGE)
        return False

#Task 7
def get_command(board: list[list[str]]) -> str:
    command = input(ENTER_COMMAND_MESSAGE)

    while not is_valid(command, board):
        command = input(ENTER_COMMAND_MESSAGE)

    return command

#Task 8
def can_flip_line(board: list[list[str]], pos: tuple[int, int], direction: str, player: str) -> bool:
    count_opponent_pieces = 0
    next_pos = (pos[0] + DIRECTIONS.get(direction)[0], pos[1] + DIRECTIONS.get(direction)[1])

    while next_pos[0] >= 0 and next_pos[0] < get_board_size(board) and next_pos[1] >= 0 and next_pos[1] < get_board_size(board):
        if (count_opponent_pieces < 1 and board[next_pos[0]][next_pos[1]] == player) or board[next_pos[0]][next_pos[1]] == EMPTY:
            return False
        elif count_opponent_pieces >=1 and board[next_pos[0]][next_pos[1]] == player:
            return True
        elif board[next_pos[0]][next_pos[1]] != player and board[next_pos[0]][next_pos[1]] != EMPTY:   
            count_opponent_pieces+=1
            pos = next_pos

        next_pos = (pos[0] + DIRECTIONS.get(direction)[0], pos[1] + DIRECTIONS.get(direction)[1])

    return False

#Task 9 -> need to update the position where player has played
def flip_line(board: list[list[str]], pos: tuple[int, int], direction: str, player: str) -> None:
    next_pos = (pos[0] + DIRECTIONS.get(direction)[0], pos[1] + DIRECTIONS.get(direction)[1])
    
    while board[next_pos[0]][next_pos[1]] != player:
        board[next_pos[0]][next_pos[1]] = player
        pos = next_pos    
        next_pos = (pos[0] + DIRECTIONS.get(direction)[0], pos[1] + DIRECTIONS.get(direction)[1]) 
      
#Task 10
def can_make_move(board: list[list[str]], pos: tuple[int, int], player: str) -> bool:
    if pos[0] >= 0 and pos[0] < get_board_size(board) and pos[1] >= 0 and pos[1] < get_board_size(board) and board[pos[0]][pos[1]] == EMPTY:
        for direction in DIRECTIONS.keys():
            if can_flip_line(board,pos,direction,player):
                return True

    return False

#Task 11
def make_move(board: list[list[str]], pos: tuple[int, int], player: str) -> None:
    #Already been checked for move validity
    board[pos[0]][pos[1]] = player
    for direction in DIRECTIONS.keys():
        if can_flip_line(board, pos, direction, player):
            flip_line(board, pos, direction, player)

#Task 12
def has_valid_move(board: list[list[str]], player: str) -> bool:
    for i in range(0, get_board_size(board)):
        for j in range(0,get_board_size(board)):
            if can_make_move(board, (i, j), player):
                return True
    return False

#Task 13
def play_game() -> None:
    print(WELCOME_MESSAGE)
    board_size = int(input("Please enter a board size between 4 and 9 (inclusive): "))
    while not (board_size >= 4 and board_size <= 9):
        board_size = int(input("Please enter a board size between 4 and 9 (inclusive): "))

    board = create_initial_board(board_size)
    current_player = PLAYER_1

    while True:
        display(board)
        if current_player == PLAYER_1:
            print(PLAYER1_TURN_MESSAGE)
        elif current_player == PLAYER_2:
            print(PLAYER2_TURN_MESSAGE)

        while True:
            command = get_command(board)
            if command in HELP_COMMAND:
                print(HELP_MESSAGE)
            elif command in QUIT_COMMAND:
                return
            else:
                row = int(command[0]) - 1
                col = int(command[2]) - 1
                if can_make_move(board, (row, col), current_player):
                    break
                else:
                    print(INVALID_MOVE_MESSAGE)

        make_move(board,(row,col), current_player)
        current_player = get_opponent(current_player)

        if not has_valid_move(board,current_player):
            print(NO_VALID_MOVE_MESSAGE)
            show_outcome(board)
            break

if __name__ == "__main__":
    play_game()