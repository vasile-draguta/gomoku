from unittest import TestCase

from domain.board import Board
from game_service.game_services import GameService


class TestGameService(TestCase):
    def test_player_win(self):
        board = Board()
        self.game_service = GameService(board)
        self.game_service.make_move(0, 0, '0')
        self.game_service.make_move(0, 1, '0')
        self.game_service.make_move(0, 2, '0')
        self.game_service.make_move(0, 3, '0')
        self.game_service.make_move(0, 4, '0')
        self.assertEqual(self.game_service.check_game_state(0, 4, '0'), 1)

    def test_ai_win(self):
        board = Board()
        self.game_service = GameService(board)
        self.game_service.make_move(1, 0, 'X')
        self.game_service.make_move(1, 1, 'X')
        self.game_service.make_move(1, 2, 'X')
        self.game_service.make_move(1, 3, 'X')
        self.game_service.make_move(1, 4, 'X')
        self.assertEqual(self.game_service.check_game_state(1, 4, 'X'), -1)

    def test_game_still_going(self):
        board = Board()
        self.game_service = GameService(board)
        self.game_service.make_move(1, 0, 'X')
        self.assertEqual(self.game_service.check_game_state(1, 0, 'X'), 111)
