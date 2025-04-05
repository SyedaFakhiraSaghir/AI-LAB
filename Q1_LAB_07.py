# Tic-Tac-Toe is a classic two-player game played on a 3×3 grid. The players take turns
# marking a space with their symbol (X or O). The goal is to form a straight line of three
# symbols, either horizontally, vertically, or diagonally. If the grid is full and no player
# has won, the game ends in a draw.
# In this task, you will implement an AI player using the Minimax algorithm. The AI will
# analyze the game board and always make the optimal move, ensuring that it never
# loses.
# 3.1.1. Game Flow
# 1. Start of the Game
# ○ The board starts empty.
# ○ The human player is assigned the symbol O, and the AI is assigned X.
# ○ The game alternates between the human and AI.
# 2. Human Player’s Turn
# ○ The player enters their move as row and column indices (0-2).
# ○ If the move is valid, it is placed on the board.
# ○ If the move is invalid (already occupied), the player is asked to try again.
# 3. AI’s Turn
# ○ The AI calculates the best move using the Minimax algorithm.
# ○ The AI places its X on the board at the optimal position.

# 4. Winning or Drawing Condition
# ○ After every move, the program checks for a winner.
# ○ If a player has won, the game announces the winner.
# ○ If the board is full with no winner, the game ends in a draw.
# Tic-Tac-Toe is a classic two-player game played on a 3×3 grid. The players take turns
# marking a space with their symbol (X or O). The goal is to form a straight line of three
# symbols, either horizontally, vertically, or diagonally. If the grid is full and no player
# has won, the game ends in a draw.
# In this task, you will implement an AI player using the Minimax algorithm. The AI will
# analyze the game board and always make the optimal move, ensuring that it never
# loses.
# 3.1.1. Game Flow
# 1. Start of the Game
# ○ The board starts empty.
# ○ The human player is assigned the symbol O, and the AI is assigned X.
# ○ The game alternates between the human and AI.
# 2. Human Player’s Turn
# ○ The player enters their move as row and column indices (0-2).
# ○ If the move is valid, it is placed on the board.
# ○ If the move is invalid (already occupied), the player is asked to try again.
# 3. AI’s Turn
# ○ The AI calculates the best move using the Minimax algorithm.
# ○ The AI places its X on the board at the optimal position.

# 4. Winning or Drawing Condition
# ○ After every move, the program checks for a winner.
# ○ If a player has won, the game announces the winner.
# ○ If the board is full with no winner, the game ends in a draw.
import random

def start_game():
  print("Welcome to Tic Tac Toe!")
  board = [[" " for _ in range(3)] for _ in range(3)]
  human = "O"
  AI = "X"
  return board, human, AI

def is_valid(row, column, board):
  if row < 0 or row > 2 or column < 0 or column > 2:
    return False
  if board[row][column] != " ":
    return False
  return True

def play(board, player):
  flag = 1
  game = 1
  while flag:
    if player == "O":
      row = int(input("Enter the row (0-2): "))
      column = int(input("Enter the column (0-2): "))
    else:
      row, column = find_best_move(board)

    if is_valid(row, column, board):
      board[row][column] = player
      flag = 0
    else:
      if player == "O":
        print("Invalid move. Try again.")
      flag = 1

    if check_win(board, player):
      if player == "O":
        print("Human wins!")
      else:
        print("AI wins!")
      game = 0
      return board, game
  return board, game

def check_win(board, player):
  for i in range(3):
    if board[i][0] == board[i][1] == board[i][2] == player:
      return True
  for i in range(3):
    if board[0][i] == board[1][i] == board[2][i] == player:
      return True
  if board[0][0] == board[1][1] == board[2][2] == player:
    return True
  if board[0][2] == board[1][1] == board[2][0] == player:
    return True
  return False

def game_over(board):
  for row in range(3):
    for col in range(3):
      if board[row][col] == " ":
        return True
  return False

def find_best_move(board):
  best_score = -float("inf")
  best_move = None

  for row in range(3):
    for col in range(3):
      if board[row][col] == " ":
        board[row][col] = "X"
        score = minimax(board, 0, False)
        board[row][col] = " "

        if score > best_score:
          best_score = score
          best_move = (row, col)
  if best_move is None:
    print("Game Over, No more valid moves!")
    return 0, 0 

  return best_move

def minimax(board, depth, is_maximizing):
  if check_win(board, "X"):
    return 1
  if check_win(board, "O"):
    return -1
  if not game_over(board):
    return 0
  if is_maximizing:
    best_score = -float("inf")
    for row in range(3):
      for col in range(3):
        if board[row][col] == " ":
          board[row][col] = "X"
          score = minimax(board, depth + 1, False)
          board[row][col] = " "
          best_score = max(score, best_score)
    return best_score
  else:
    best_score = float("inf")
    for row in range(3):
      for col in range(3):
        if board[row][col] == " ":
          board[row][col] = "O"
          score = minimax(board, depth + 1, True)
          board[row][col] = " "
          best_score = min(score, best_score)
    return best_score

def display(board):
  for row in board:
    print(" | ".join(row))

# Start the game
board, human, AI = start_game()
game_overr = True
while game_overr:
  game_overr = game_over(board)
  print("Human's turn")
  board, game = play(board, human)
  if not game:
    break
  display(board)
  print("AI's turn")
  board, game = play(board, AI)
  if not game:
    break
  display(board)
