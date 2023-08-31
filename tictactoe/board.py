# board.py

class Position:
    """
    Represents the x and y coordinates of a slot on the TicTacToe board.
    """
    def __init__(self, x, y):
        """
        Initialize a position with x and y coordinates.

        -Args:
        x-coordinate: int
        y-coordinate: int
        """
        self.x = x
        self.y = y


class Slot:
    """
    Represents a single slot on the TicTacToe board.
    """
    def __init__(self, position, symbol=None):
        """
        Initialize a slot with a given position and an optional symbol.

        -Args:
        position(Position object representing slot's location)
        symbol(Symbol for the slot ('X', 'O', etc.). Defaults to None)
        """
        self.position = position
        self.symbol = symbol


class Board:
    """
    Represents the entire TicTacToe board.
    """
    def __init__(self, size):
        """
        Initialize a board of given size.

        -Args:
        size(Size of the board (e.g., 3 for a 3x3 board))
        """
        self.size = size
        self.slots = [[Slot(Position(i, j)) for j in range(size)] for i in range(size)]

    def displayBoard(self):
        """
        Display the current state of the board with enhanced formatting.
        """
        for i, row in enumerate(self.slots):
            if i:
                print('-' * (4 * len(row) - 1))  # Print horizontal separator line
            for j, slot in enumerate(row):
                # Decide if we need a separator or a new line
                end_char = ' | ' if j < len(row) - 1 else '\n'
                print(' ' + (slot.symbol if slot.symbol else '.'), end=end_char)

    def isFull(self):
        """
        Check if the board is full (no empty slots).

        -Returns:
        Boolean: True if the board is full, False otherwise.
        """
        for row in self.slots:
            for slot in row:
                if not slot.symbol:
                    return False
        return True
