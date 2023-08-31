# TicTacToe-LLD

## Table of Contents
1. [Introduction](#introduction)
2. [ClassDiagram](#classdiagram)
3. [ClassDescriptions](#classdescriptions)
4. [GameFlow](#gameflow)
5. [RunningGame](#runninggame)
6. [Conclusion](#conclusion)

### Introduction
This document details the low-level design of a TicTacToe game, outlining the classes, methods, and functionality.

### ClassDiagram
![image](https://github.com/codingis4noobs2/TicTacToe-LLD/assets/87560178/cdb56cfd-8e40-4f38-82d7-bc3f6845c74c)

### ClassDescriptions
#### Board
Represents the TicTacToe game board.

**Attributes**:

**size**: The size of the board (e.g., 3 for a 3x3 board).

**slots**: 2D list containing Slot objects.

##### Methods:

**displayBoard()**: Displays the current state of the board.

**isFull()**: Checks if the board is full.

---

#### Slot
Represents a single slot in the TicTacToe game board.

**Attributes**:

**position**: The position of the slot on the board.

**symbol**: The symbol placed in the slot (e.g., "X" or "O").

#### Position
Represents a position on the TicTacToe game board.

**Attributes**:

**x**: X-coordinate of the position.

**y**: Y-coordinate of the position.

---

#### Player

Represents a player or bot in the game.

**Attributes**:

**name**: Name of the player.

**symbol**: Symbol chosen by the player.

**isBot**: Flag indicating if the player is a bot.

**move_history**: List of moves made by the player.

---

#### TicTacToe

Represents the main game logic.

**Attributes**:

**board**: The game board.

**players**: List of Player objects.

**current_player_index**: Index of the current player.

**row_counts, col_counts, diag_counts**: Lists to keep track of the counts of each row, column, and diagonal.

##### Methods:

**startGame()**: Main game loop.

**makeMove(player)**: Handles player's moves.

**botMove()**: Determines bot's move.

**checkWinner()**: Checks if the current player has won.

**undoMove(player)**: Undoes the last move made by the player.

### GameFlow
1. Initialize the game by taking user input for player details and board size.
2. Display the board.
3. Loop until the board is full or a player has won:
   - Take the current player's move.
   - Check if they have won.
   - Switch to the next player.
  Display the game result.

### RunningGame
To play the game, run the tictactoe_game.py file present inside tictactoe folder.

### Conclusion
The low-level design of the TicTacToe game provides a detailed overview of the classes, attributes, methods, and game flow. The game supports both human players and bot players.
