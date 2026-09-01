
EMPTY = "."
PLAYER_1 = "X"
PLAYER_2 = "O"

SEP = "-" * 20

HELP_COMMAND = ["h", "H"]
QUIT_COMMAND = ["q", "Q"]

DIRECTIONS = {
    "right": (0, 1),
    "left": (0, -1),
    "up": (-1, 0),
    "down": (1, 0),
    "up-right": (-1, 1),
    "up-left": (-1, -1),
    "down-right": (1, 1),
    "down-left": (1, -1)
}

HELP_MESSAGE = """
Commands:
- Enter a move as row,col
  Example: 2,5
- h/H: Display help
- q/Q: Quit game
"""

WELCOME_MESSAGE = "\nWelcome to Reversi!\n"

ENTER_COMMAND_MESSAGE = "Enter your move: "

INVALID_COMMAND_MESSAGE = "Invalid command."
INVALID_MOVE_MESSAGE = "That move is not valid."
NO_VALID_MOVE_MESSAGE = "No valid moves are available. Game over."

PLAYER1_TURN_MESSAGE = "Player 1 (X) turn"
PLAYER2_TURN_MESSAGE = "Player 2 (O) turn"


PLAYER1_WIN_MESSAGE = "Player 1 wins!"
PLAYER2_WIN_MESSAGE = "Player 2 wins!"
DRAW_MESSAGE = "The game is a draw."

def put_initial_pieces(board: list[list[str]]) -> None:
    """
    Place the initial pieces on the board.

    Parameters:
        board: The game board. 
        size: The number of rows or columns in the square board.
    """

    size  = len(board)
    board[size//2 - 1][size//2 -1] = PLAYER_1
    board[size//2][size//2] = PLAYER_1
    board[size//2 - 1][size//2] = PLAYER_2
    board[size//2][size//2 - 1] = PLAYER_2


def get_opponent(player: str) -> str:
    """
    Return the opponent's piece.

    Parameters:
        player: The current player.

    Returns:
        The opponent's piece.
    """

    if player == PLAYER_1:
        return PLAYER_2

    return PLAYER_1
