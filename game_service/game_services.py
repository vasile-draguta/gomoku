class GameService:
    def __init__(self, board):
        self.gomoku_board = board

    def get_board(self):
        return self.gomoku_board.get_board()

    @staticmethod
    def check_for_five_consecutive_symbols(line, symbol):
        """
        Checks if a line contains 5 consecutive symbols
        :param line: line to be checked
        :param symbol: symbol to be checked
        :return: True if the line contains 5 consecutive symbols, False otherwise
        """
        symbol_count = 0
        for cell in line:
            if cell == symbol:
                symbol_count += 1
                if symbol_count == 5:
                    return True
            else:
                symbol_count = 0
        return False

    def check_winner(self, last_move_row, last_move_column, symbol):
        """
        Creates a line for each direction,starting from the last move and checks if it contains 5 consecutive
        symbols to determine if there is a winner
        :param last_move_row: Last move's row
        :param last_move_column: Last move's column
        :param symbol: Symbol of the last move
        :return: True if there is a winner, False otherwise
        """
        # Check horizontally
        if GameService.check_for_five_consecutive_symbols(self.gomoku_board.get_board()[last_move_row], symbol):
            return True

        # Check vertically, creating a list with the column values
        if GameService.check_for_five_consecutive_symbols([self.gomoku_board.get_board()[i][last_move_column] for i in range(15)], symbol):
            return True

        # Check diagonally, creating a list with the diagonal values
        if GameService.check_for_five_consecutive_symbols([self.gomoku_board.get_board()[i][j] for i, j in zip(range(last_move_row, -1, -1), range(last_move_column, -1, -1))], symbol):
            return True
        if GameService.check_for_five_consecutive_symbols([self.gomoku_board.get_board()[i][j] for i, j in zip(range(last_move_row, 15), range(last_move_column, -1, -1))], symbol):
            return True

        return False

    def check_game_state(self, last_move_row, last_move_column, last_symbol):
        """
        Uses the check_winner method to determine if there is a winner or if the game is still running
        :param last_move_row: Row of the last move
        :param last_move_column: Column of the last move
        :param last_symbol: Last move's symbol
        :return: 1 if 0 won, -1 if X won, 0 if it's a draw, 111 if the game is still running
        """
        exist_winner = self.check_winner(last_move_row, last_move_column, last_symbol)

        if exist_winner and last_symbol == '0':
            return 1    # 0 won
        elif exist_winner and last_symbol == 'X':
            return -1   # X won
        elif self.gomoku_board.get_number_of_moves() == 225:
            return 0    # Draw
        else:
            return 111  # Game is still running

    def make_move(self, row, column, player_symbol):
        """
        Makes a move on the board
        :param row: Row index
        :param column: Column index
        :param player_symbol: Symbol of the player or the AI
        :return: None
        """
        self.gomoku_board.make_move(row, column, player_symbol)
