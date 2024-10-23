class Board:
    def __init__(self):
        ROWS = 15
        COLUMNS = 15
        self.board = [[' '] * ROWS for _ in range(COLUMNS)]  # creates a 15x15 empty board
        self.moves_count = 0

    def get_board(self):
        return self.board

    def get_number_of_moves(self):
        return self.moves_count

    def is_position_available(self, row, column):
        """
        Checks if the position is available
        :param row: Row index
        :param column: Column index
        :return: True if the position is available, False otherwise
        """
        ROWS = 15
        COLUMNS = 15
        if row not in range(ROWS) or column not in range(COLUMNS):
            raise ValueError("Invalid position")
        if self.board[row][column] == ' ':
            return True
        return False

    def make_move(self, row, column, player_symbol):
        """
        Makes a move on the board
        :param row: Row index
        :param column: Column index
        :param player_symbol: The symbol of the player or the AI
        :return: None
        """
        ROWS = 15
        COLUMNS = 15
        if self.is_position_available(row, column) and row in range(ROWS) and column in range(COLUMNS):
            self.board[row][column] = player_symbol
            self.moves_count += 1
            return
        raise ValueError("Position not available")
