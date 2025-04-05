import chess
import chess.engine

# start the game
def start_game():
    print("AI playing Chess!")
    return chess.Board()

# display the chessboard
def display(board):
    print(board)

# evaluate the board (based on piece values)
def evaluate_board(board):
    piece_values = {"K": 0, "Q": 9, "R": 5, "B": 3, "N": 3, "P": 1}
    score = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            score += piece_values.get(piece.symbol().upper(), 0) * (1 if piece.color == chess.WHITE else -1)
    return score

# minimax algorithm with alpha-beta pruning (AI decision making)
def minimax(board, depth, alpha, beta, is_maximizing, player):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)

    if is_maximizing:
        max_eval = -float("inf")
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, False, chess.BLACK if player == chess.WHITE else chess.WHITE)
            board.pop()
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float("inf")
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, True, chess.WHITE if player == chess.BLACK else chess.BLACK)
            board.pop()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# AI finds the best move based on minimax
def find_best_move(board, player, depth=3):
    best_move = None
    best_value = -float("inf") if player == chess.WHITE else float("inf")
    for move in board.legal_moves:
        board.push(move)
        move_value = minimax(board, depth, -float("inf"), float("inf"), False, chess.BLACK if player == chess.WHITE else chess.WHITE)
        board.pop()
        if (player == chess.WHITE and move_value > best_value) or (player == chess.BLACK and move_value < best_value):
            best_value = move_value
            best_move = move
    return best_move

# run the game loop where both AIs play
def play_game():
    board = start_game()

    AI_1 = input("Enter name for 1st AI BOT: ")
    AI_2 = input("Enter name for 2nd AI BOT: ")

    print(f"\n{AI_1} is playing with white pieces and {AI_2} is playing with black pieces")

    display(board)

    turn = chess.WHITE  # AI_1 starts first (uppercase)
    while not board.is_game_over():
        if turn == chess.WHITE:  # AI_1's turn
            print(f"\n{AI_1}'s turn:")
            move = find_best_move(board, chess.WHITE)
            print(f"{AI_1} moves {move}")
            board.push(move)
            display(board)
            turn = chess.BLACK
        else:  # AI_2's turn
            print(f"\n{AI_2}'s turn:")
            move = find_best_move(board, chess.BLACK)
            print(f"{AI_2} moves {move}")
            board.push(move)
            display(board)
            turn = chess.WHITE

    print("\nGame Over!")
    print(board.result())


play_game()
