from board_evaluation import count_continuous_x
from unittest import TestCase


class TestCountX(TestCase):

    def test_three_small_board(self):
        board = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ]
        result = count_continuous_x(board, 1, 3)
        self.assertEqual(1, result)

    def test_no_three_in_four(self):
        board = [
            [1, 0, 0, 0],
            [1, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 1]
        ]
        result = count_continuous_x(board, 1, 3)
        self.assertEqual(1, result)

    def count_multiple_three(self):
        board = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        result = count_continuous_x(board, 1, 3)
        self.assertEqual(8, result)
