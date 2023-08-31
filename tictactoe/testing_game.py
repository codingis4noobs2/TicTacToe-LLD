import unittest
from board import Board, Slot, Position
from player import Player
from tictactoe_game import TicTacToe

class TestTicTacToe(unittest.TestCase):
    
    def test_position_initialization(self):
        position = Position(1, 2)
        self.assertEqual(position.x, 1)
        self.assertEqual(position.y, 2)

    def test_slot_initialization(self):
        position = Position(1, 2)
        slot = Slot(position)
        self.assertEqual(slot.position, position)
        self.assertIsNone(slot.symbol)

    def test_board_initialization(self):
        board = Board(3)
        self.assertEqual(board.size, 3)
        self.assertEqual(len(board.slots), 3)
        self.assertEqual(len(board.slots[0]), 3)
        self.assertIsInstance(board.slots[0][0], Slot)

    def test_player_move_history(self):
        player = Player("TestPlayer", "X")
        self.assertEqual(player.move_history, [])
        position = Position(1, 2)
        player.move_history.append(position)
        self.assertEqual(player.move_history, [position])

    def test_tictactoe_initialization(self):
        player1 = Player("Player1", "X")
        player2 = Player("Player2", "O", isBot=True)
        game = TicTacToe(3, [player1, player2])
        self.assertEqual(game.board.size, 3)
        self.assertEqual(game.players, [player1, player2])
        self.assertEqual(game.current_player_index, 0)
        self.assertEqual(game.row_counts, [0, 0, 0])
        self.assertEqual(game.col_counts, [0, 0, 0])
        self.assertEqual(game.diag_counts, [0, 0])

if __name__ == "__main__":
    unittest.main()
