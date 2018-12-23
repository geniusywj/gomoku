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
        result_three = count_continuous_x(board, 1, 3)
        result_four = count_continuous_x(board, 1, 4)
        self.assertEqual(1, result_three)
        self.assertEqual(1, result_four)

    def test_full_board_three(self):
        board = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        result = count_continuous_x(board, 1, 3)
        self.assertEqual(8, result)

    def test_full_board_four(self):
        board = [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1]
        ]
        result_three = count_continuous_x(board, 1, 3)
        result_four = count_continuous_x(board, 1, 4)
        self.assertEqual(4, result_three)
        self.assertEqual(10, result_four)
