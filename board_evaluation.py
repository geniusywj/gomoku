from itertools import product


# four is not counted as three
def count_continuous_x(board, player, x):
    board_size = len(board)
    offsets = ((0, 1), (1, 1), (1, 0), (1, -1))
    count = 0
    for i, j in product(range(board_size - x + 1), range(board_size - x + 1)):
        if board[i][j] == player:
            for offset in offsets:
                if i - offset[0] >= 0 and j - offset[1] >= 0 and board[i - offset[0]][j - offset[0]] == player:
                    continue
                if all(board[i + offset[0] * x_][j + offset[1] * x_] == player for x_ in range(1, x)):
                    if i + offset[0] * x < board_size and j + offset[1] * x < board_size:
                        count += board[i + offset[0] * x][j + offset[1] * x] != player
                    else:
                        count += 1
    return count
