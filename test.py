from board_evaluation import count_pattern, BORDER, EMPTY, ME, OPPONENT
from unittest import TestCase


class TestPattern(TestCase):

    def test_living_five(self):
        pattern = [ME] * 5
        board = [
            [1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        result = count_pattern(board, pattern)
        self.assertEqual(1, result)
