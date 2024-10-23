from domain.ai import AI
from domain.board import Board
from game_service.game_services import GameService
from ui.console_ui import ConsoleUI

if __name__ == "__main__":
    board = Board()
    ai = AI(board)
    game_service = GameService(board)
    ui = ConsoleUI(game_service, ai)
    ui.run_game()
