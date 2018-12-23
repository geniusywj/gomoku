import copy


class SearchAgent:

    NEGATIVE_INFINITY = 'NEGATIVE_INFINITY'
    POSITIVE_INFINITY = 'POSITIVE_INFINITY'

    def __init__(self, board, player, depth):
        self.depth = depth
        self.player = player
        self.board = board

    def update_board(self, board):
        self.board = board

    def get_action(self):
        def max_value(board, alpha, beta, depth):
            if self.is_win(board) or self.is_lose(board) or depth == self.depth:
                return self.evaluate_state(board)

            v = self.NEGATIVE_INFINITY
            for action in self.get_legal_action(board):
                next_board = self.get_successor(board, action)
                v_ = min_value(next_board, alpha, beta, depth + 1)
                v = v_ if v == self.NEGATIVE_INFINITY else max(v, v_)
                if beta != self.POSITIVE_INFINITY and v > beta:
                    return v
                alpha = v if alpha == self.NEGATIVE_INFINITY else max(alpha, v)
            return v

        def min_value(board, alpha, beta, depth):
            if self.is_win(board) or self.is_lose(board) or depth == self.depth:
                return self.evaluate_state(board)

            v = self.POSITIVE_INFINITY
            for action in self.get_legal_action(board):
                next_board = self.get_successor(board, action)
                v_ = max_value(next_board, alpha, beta, depth + 1)
                v = v_ if v == self.POSITIVE_INFINITY else min(v, v_)
                if alpha != self.NEGATIVE_INFINITY and v < alpha:
                    return v
                beta = v if beta == self.POSITIVE_INFINITY else min(beta, v)
            return v
        
        return max_value(self.board, self.NEGATIVE_INFINITY, self.POSITIVE_INFINITY, 0)

    def get_legal_action(self, board):
        return []

    def get_successor(self, board, action):
        next_board = copy.deepcopy(board)
        next_board[action[0]][action[1]] = self.player
        return next_board

    def evaluate_state(self, board):
        return 0

    def is_win(self, board):
        return True

    def is_lose(self, board):
        return True
