from itertools import product

BORDER = -1
EMPTY = 0
ME = 1
OPPONENT = 2


def count_pattern(board_without_border, pattern):
    count = 0

    # add border to the board
    board_size = len(board_without_border) + 2
    board = list()
    board.append([BORDER] * board_size)
    for row in board_without_border:
        board.append([BORDER] + row.copy() + [BORDER])
    board.append([BORDER] * board_size)

    offsets = list(product((-1, 0, 1), (-1, 0, 1)))
    offsets.remove((0, 0))
    for i, j in product(range(board_size), repeat=2):
        if board[i][j] == pattern[0]:
            for offset in offsets:
                try:
                    count += all(board[i + offset[0] * x][j + offset[1] * x] == p for x, p in enumerate(pattern))
                except IndexError:
                    continue

    return count // 2 if pattern == pattern[::-1] else count
