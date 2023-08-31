# tictactoe_game.py

import random
from board import Board, Slot, Position
from player import Player

class TicTacToe:
    """
    Represents the main TicTacToe game logic.
    """

    def __init__(self, board_size, players):
        """
        Initializes the TicTacToe game.

        -Args:
        board_size(Size of the board (e.g., 3 for a 3x3 board))
        players(List of Player objects participating in the game)
        """
        self.board = Board(board_size)
        self.players = players
        self.current_player_index = 0
        self.row_counts = [0] * board_size
        self.col_counts = [0] * board_size
        self.diag_counts = [0, 0]

    def startGame(self):
        """
        Main loop to play the TicTacToe game.
        """
        while True:
            print("\nCurrent Board State:\n")
            self.board.displayBoard()
            print("\n")
            
            if self.board.isFull():
                print("The game is a draw!")
                break

            self.makeMove(self.players[self.current_player_index])
            
            if self.checkWinner():
                print("\nFinal Board State:")
                self.board.displayBoard()
                print(f"\n{self.players[self.current_player_index].name} wins!\n")
                break
                
            self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def makeMove(self, player):
        """
        Handle player's move, including the bot's moves.

        -Args:
        player(Current Player object making the move)
        """
        while True:
            try:
                if player.isBot:
                    x, y = self.botMove()
                else:
                    move = input(f"{player.name}, enter your move (x y) or type 'undo': ").strip().lower()
                    if move == "undo":
                        if not player.move_history:
                            print("You haven't made any moves yet!")
                            continue
                        self.undoMove(player)
                        return
                    x, y = map(int, move.split())
                # Validate move
                if 0 <= x < len(self.board.slots) and 0 <= y < len(self.board.slots):
                    if self.board.slots[x][y].symbol is None:
                        self.board.slots[x][y].symbol = player.symbol
                        symbol_value = 1 if player.symbol == self.players[0].symbol else -1
                        self.row_counts[x] += symbol_value
                        self.col_counts[y] += symbol_value
                        if x == y:
                            self.diag_counts[0] += symbol_value
                        if x + y == len(self.board.slots) - 1:
                            self.diag_counts[1] += symbol_value
                        player.move_history.append(Position(x, y))
                        return
                    else:
                        print("Slot already occupied. Try again.")
                else:
                    print("Invalid coordinates.")
            except ValueError:
                print("Invalid input.")

    def botMove(self):
        """
        Calculate the bot's move using random choice from available slots.

        -Returns:
        Tuple: Representing the bot's chosen move.
        """
        available_slots = [(i, j) for i in range(self.board.size) for j in range(self.board.size) if self.board.slots[i][j].symbol is None]
        return random.choice(available_slots)

    def checkWinner(self):
        """
        Check if the current player has won the game.

        -Returns:
        Boolean: True if the current player has won, False otherwise.
        """
        n = len(self.board.slots)
        return any(abs(count) == n for count in self.row_counts + self.col_counts + self.diag_counts)

    def undoMove(self, player):
        """
        Undo the last move made by the player.

        -Args:
        player(Current Player object to undo the move for)
        """
        last_move = player.move_history.pop()
        self.board.slots[last_move.x][last_move.y].symbol = None
        symbol_value = 1 if player.symbol == self.players[0].symbol else -1
        self.row_counts[last_move.x] -= symbol_value
        self.col_counts[last_move.y] -= symbol_value
        if last_move.x == last_move.y:
            self.diag_counts[0] -= symbol_value
        if last_move.x + last_move.y == len(self.board.slots) - 1:
            self.diag_counts[1] -= symbol_value
        self.current_player_index = (self.current_player_index - 1) % len(self.players)

def initialize_game():
    """
    Sets up the TicTacToe game by taking user input for player details and board size.
    """
    player1_name = input("Enter the name of Player 1: ")
    player1_symbol = input(f"{player1_name}, please choose your symbol: ")
    player1 = Player(player1_name, player1_symbol)

    available_symbols = ["X", "O", "#", "@", "$"]
    available_symbols.remove(player1_symbol)  # Remove chosen symbol from available options

    player2_type = ""
    while player2_type not in ["yes", "no"]:
        player2_type = input(f"Is Player 2 a bot? (yes/no): ").lower()
    
    isBot = player2_type == "yes"
    
    if isBot:
        player2_name = "Bot"
        player2_symbol = random.choice(available_symbols)
    else:
        player2_name = input(f"Enter the name of Player 2: ")
        while True:
            player2_symbol = input(f"{player2_name}, please choose your symbol from {available_symbols}: ")
            if player2_symbol in available_symbols:
                break
            print(f"Invalid symbol. Please choose from {available_symbols}.")

    player2 = Player(player2_name, player2_symbol, isBot)

    board_size = int(input("Enter the board size: "))
    game = TicTacToe(board_size, [player1, player2])
    game.startGame()

if __name__ == "__main__":
    initialize_game()
