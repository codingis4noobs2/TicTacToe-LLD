# player.py

class Player:
    """
    Represents a player in the TicTacToe game.
    """
    def __init__(self, name, symbol, isBot=False):
        """
        Initialize a player with a given name, symbol, and an optional bot flag.

        -Args
        name(Name of the player)
        symbol(Symbol chosen by the player ('X', 'O', etc.))
        isBot(Boolean indicating whether the player is a bot. Defaults to False)
        """
        self.name = name
        self.symbol = symbol
        self.isBot = isBot
        self.move_history = []  # List to track the moves made by this player
