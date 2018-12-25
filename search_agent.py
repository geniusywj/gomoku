import copy
from board_evaluation import count_pattern, BORDER, EMPTY, ME, OPPONENT


class SearchAgent:
    NEGATIVE_INFINITY = 'NEGATIVE_INFINITY'
    POSITIVE_INFINITY = 'POSITIVE_INFINITY'
    depth = 5

    def __init__(self, board, player, opponent):
        self.player = player
        self.opponent = opponent
        self.board = board

    def update_board(self, board):
        self.board = board

    def get_action(self):
        def max_value(board, alpha, beta, depth):
            if self.is_win(board):
                return 10000
            if self.is_lose(board):
                return -10000
            if depth == self.depth:
                return self.evaluate_state(board)

            v = self.NEGATIVE_INFINITY
            desired_action = None
            for action in self.get_legal_action(board):
                next_board = self.get_successor(board, action)
                v_ = min_value(next_board, alpha, beta, depth)
                v, desired_action = (v_, action) if v == self.NEGATIVE_INFINITY or v_ > v else (v, desired_action)
                if beta != self.POSITIVE_INFINITY and v > beta:
                    return v, desired_action
                alpha = v if alpha == self.NEGATIVE_INFINITY else max(alpha, v)
            return v, desired_action

        def min_value(board, alpha, beta, depth):
            if self.is_win(board):
                return 10000
            if self.is_lose(board):
                return -10000

            v = self.POSITIVE_INFINITY
            desired_action = None
            for action in self.get_legal_action(board):
                next_board = self.get_successor(board, action)
                v_ = max_value(next_board, alpha, beta, depth + 1)
                v, desired_action = (v_, action) if v == self.POSITIVE_INFINITY or v_ < v else (v, desired_action)
                if alpha != self.NEGATIVE_INFINITY and v < alpha:
                    return v, desired_action
                beta = v if beta == self.POSITIVE_INFINITY else min(beta, v)
            return v, desired_action

        _, action_to_take = max_value(self.board, self.NEGATIVE_INFINITY, self.POSITIVE_INFINITY, 0)
        return action_to_take

    def get_legal_action(self, board):
        return []

    def get_successor(self, board, action):
        next_board = copy.deepcopy(board)
        next_board[action[0]][action[1]] = self.player
        return next_board

    def evaluate_state(self, board):
        patterns = {
            'living four': ([EMPTY] + [ME] * 4 + [EMPTY],),
            'dead four': ([OPPONENT] + [ME] * 4 + [EMPTY], [BORDER] + [ME] * 4 + [EMPTY], [ME] + [EMPTY] + [ME] * 3,
                          [ME] * 2 + [EMPTY] + [ME] * 2),
            'living three': ([EMPTY] * 2 + [ME] * 3 + [EMPTY], [EMPTY] + [ME] + [EMPTY] + [ME] * 2 + [EMPTY]),
            'dead three': ([ME] + [EMPTY] + [ME] + [EMPTY] + [ME], [ME] * 2 + [EMPTY] * 2 + [ME],
                           [OPPONENT] + [ME] * 3 + [EMPTY] * 2, [BORDER] + [ME] * 3 + [EMPTY] * 2,
                           [OPPONENT] + [ME] * 2 + [EMPTY] + [ME] + [EMPTY],
                           [OPPONENT] + [ME] + [EMPTY] + [ME] * 2 + [EMPTY],
                           [BORDER] + [ME] * 2 + [EMPTY] + [ME] + [EMPTY],
                           [BORDER] + [ME] + [EMPTY] + [ME] * 2 + [EMPTY]),
        }
        scores = {
            'living four': 1000,
            'dead four': 500,
            'living three': 200,
            'dead three': 100
        }
        score = sum(scores[pattern] * count_pattern(board, pattern) for pattern in patterns)
        return score

    def is_win(self, board):
        pattern = [ME] * 5
        return count_pattern(board, pattern)

    def is_lose(self, board):
        pattern = [OPPONENT] * 5
        return count_pattern(board, pattern)
