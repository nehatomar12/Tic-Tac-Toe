
import numpy as np
import random

def create_game_board():
    return np.array([[0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]])

### Random find the empty block and get the place ###


def get_empty_block(game_board):
    empty_blocks = []
    for i in range(len(game_board)):
        for j in range(len(game_board)):
            if game_board[i][j] == 0:
                empty_blocks.append((i, j))
    return empty_blocks


def pick_random_block(game_board, user):
    empty_blocks = get_empty_block(game_board)
    current_block = random.choice(empty_blocks)
    game_board[current_block] = user
    return game_board


####################################################

#### Evaluate winner #########

def row_win(game_board):
    global winner, winner_user
    for i in range(game_board.shape[0]):
        if game_board[i][0] != 0 and np.all(game_board[i] == game_board[i][0]):
            print("Row win: ", game_board[i])
            winner = True
            winner_user = game_board[i][0]
            return winner
    return winner


def col_win(game_board):
    global winner, winner_user
    t_game_board = game_board.T
    for i in range(t_game_board.shape[0]):
        if t_game_board[i][0] != 0 and np.all(t_game_board[i] == t_game_board[i][0]):
            print("col win: ", t_game_board[i])
            winner = True
            winner_user = t_game_board[i][0]
            return winner
    return winner


def diagonal_win(game_board):
    global winner, winner_user
    diagonals = []
    diagonals.append(game_board.diagonal())
    diagonals.append(np.fliplr(game_board).diagonal())
    for d in diagonals:
        if d[0] != 0 and np.all(d == d[0]):
            print("dia win: ", d)
            winner = True
            winner_user = d[0]
            return winner
    return winner



#######################################


if __name__ == "__main__":
    winner = False
    winner_user = ""
    game_board = create_game_board()
    moves = 0

    while not winner and moves < 9:
        user = 1 if moves%2 == 0  else 2
        moves += 1
        game_board = pick_random_block(game_board, user)
        if np.all(game_board != 0):
            print("Tic Tac Toe results is Tie!!")
            break
        if row_win(game_board) or col_win(game_board) or diagonal_win(game_board):
            print("Tic Tac Toe winner is {}".format(winner_user))
            break
