from unittest import TestCase

from domain.board import Board


class TestBoard(TestCase):
    def setUp(self):
        self.board = Board()

    def test_get_board(self):
        self.assertEqual(self.board.get_board(), [[' '] * 15 for _ in range(15)])

    def test_get_number_of_moves(self):
        self.assertEqual(self.board.get_number_of_moves(), 0)

    def test_make_a_move(self):
        self.board.make_move(0, 0, '0')
        self.assertEqual(self.board.get_number_of_moves(), 1)
        self.assertEqual(self.board.get_board()[0][0], '0')

    def test_check_if_position_available(self):
        self.assertTrue(self.board.is_position_available(0, 0))
        self.board.make_move(0, 0, '0')
        self.assertFalse(self.board.is_position_available(0, 0))
