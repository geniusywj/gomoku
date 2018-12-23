from itertools import product


# four is not counted as three
def count_continuous_x(board, player, x):
    board_size = len(board)
    offsets = ((0, 1), (1, 1), (1, 0), (1, -1))
    count = 0
    for i, j in product(range(board_size), range(board_size)):
        if board[i][j] == player:
            for offset in offsets:
                if not out_of_bound(board, i - offset[0], j - offset[1]) and \
                        board[i - offset[0]][j - offset[1]] == player:
                    continue
                legal = True
                for x_ in range(1, x):
                    i_ = i + offset[0] * x_
                    j_ = j + offset[1] * x_
                    if out_of_bound(board, i_, j_):
                        legal = False
                        break
                    legal = legal and board[i_][j_] == player
                if not out_of_bound(board, i + offset[0] * x, j + offset[1] * x) and \
                        board[i + offset[0] * x][j + offset[1] * x] == player:
                    legal = False
                count += legal
    return count


def out_of_bound(board, i, j):
    return i >= len(board) or j >= len(board) or i < 0 or j < 0
