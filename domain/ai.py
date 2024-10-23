from random import choice


class AI:
    def __init__(self, board):
        self.board = board

    def pick_a_random_position(self):
        """
        Picks a random available position from the board
        :return: The position
        """
        board = self.board.get_board()
        possible_moves = [(row, col) for row in range(15) for col in range(15) if board[row][col] == ' ']
        return choice(possible_moves)

    def make_a_move(self):
        """
        Makes a move on the board, by searching for a position that is close to winning and if there is none, it picks
        a random position
        :return: The position found
        """
        board = self.board.get_board()
        ROWS = 15
        COLS = 15
        SYMBOLS_CLOSE_TO_WIN = 4
        SYMBOLS_TO_WIN = 5
        EMPTY = ' '
        PLAYER_SYMBOL = '0'

        # Check rows
        for row in range(ROWS):
            for col in range(COLS - SYMBOLS_CLOSE_TO_WIN):
                window = board[row][col:col + SYMBOLS_TO_WIN]
                if window.count(PLAYER_SYMBOL) == SYMBOLS_CLOSE_TO_WIN and window.count(EMPTY) == 1:
                    return row, col + window.index(EMPTY)

        # Check columns
        for col in range(COLS):
            for row in range(ROWS - SYMBOLS_CLOSE_TO_WIN):
                window = [board[row + i][col] for i in range(SYMBOLS_TO_WIN)]
                if window.count(PLAYER_SYMBOL) == SYMBOLS_CLOSE_TO_WIN and window.count(EMPTY) == 1:
                    return row + window.index(EMPTY), col

        # Check diagonals
        for row in range(ROWS - SYMBOLS_CLOSE_TO_WIN):
            for col in range(COLS - SYMBOLS_CLOSE_TO_WIN):
                window1 = [board[row + i][col + i] for i in range(SYMBOLS_TO_WIN)]
                window2 = [board[row + i][col + SYMBOLS_CLOSE_TO_WIN - i] for i in range(SYMBOLS_TO_WIN)]

                if window1.count(PLAYER_SYMBOL) == SYMBOLS_CLOSE_TO_WIN and window1.count(EMPTY) == 1:
                    return row + window1.index(EMPTY), col + window1.index(EMPTY)

                if window2.count(PLAYER_SYMBOL) == SYMBOLS_CLOSE_TO_WIN and window2.count(EMPTY) == 1:
                    return row + window2.index(EMPTY), col + SYMBOLS_CLOSE_TO_WIN - window2.index(EMPTY)

        return self.pick_a_random_position()
