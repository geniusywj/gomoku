import copy
import board_evaluation


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
            if self.is_win(board) or self.is_lose(board) or depth == self.depth:
                return self.evaluate_state(board)

            v = self.NEGATIVE_INFINITY
            desired_action = None
            for action in self.get_legal_action(board):
                next_board = self.get_successor(board, action)
                v_ = min_value(next_board, alpha, beta, depth + 1)
                v, desired_action = (v_, action) if v == self.NEGATIVE_INFINITY or v_ > v else (v, desired_action)
                if beta != self.POSITIVE_INFINITY and v > beta:
                    return v, desired_action
                alpha = v if alpha == self.NEGATIVE_INFINITY else max(alpha, v)
            return v, desired_action

        def min_value(board, alpha, beta, depth):
            if self.is_win(board) or self.is_lose(board) or depth == self.depth:
                return self.evaluate_state(board)

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
        return 0

    def is_win(self, board):
        return board_evaluation.count_continuous_x(board, self.player, 5)

    def is_lose(self, board):
        return board_evaluation.count_continuous_x(board, self.opponent, 5)
