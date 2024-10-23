import time
import pyautogui


class ConsoleUI:
    def __init__(self, gomoku_board, ai):
        self.console_board = gomoku_board
        self.ai = ai

    def print_board(self):
        ROWS = 15
        COLUMNS = 15
        FIRST_COLUMN = 0
        FIRST_DOUBLE_DIGITS_COLUMN = 10
        time.sleep(0.1)
        pyautogui.hotkey('alt', 'l')    # Clears the console
        board = self.console_board.get_board()
        print(f"   00  01  02  03  04  05  06  07  08  09  10  11  12  13  14")     # Prints the column numbers
        for row in range(ROWS):
            for col in range(COLUMNS):
                if col == FIRST_COLUMN:
                    if row < FIRST_DOUBLE_DIGITS_COLUMN:
                        print(f"0{row} ", end='')
                    else:
                        print(f"{row} ", end='')
                print(f"[{board[row][col]}] ", end='')
            print()

    def print_final_state(self, row, column, symbol):
        self.print_board()
        PLAYER_WIN = 1
        AI_WIN = -1
        DRAW = 0

        if self.console_board.check_game_state(row, column, symbol) == PLAYER_WIN:
            print("0 won!")
        elif self.console_board.check_game_state(row, column, symbol) == AI_WIN:
            print("X won!")
        elif self.console_board.check_game_state(row, column, symbol) == DRAW:
            print("Draw!")

    @staticmethod
    def change_symbol(symbol):
        if symbol == '0':
            return 'X'
        return '0'

    def run_game(self):
        symbol = '0'
        game_is_running = True
        ROW_INDEX = 0
        COLUMN_INDEX = 1

        while game_is_running:
            self.print_board()

            if symbol == '0':
                try:
                    user_input = input("What move do you want to make? ")
                    if user_input.lower() == 'exit':
                        game_is_running = False
                        continue
                    user_input = user_input.split()
                    row = int(user_input[ROW_INDEX])
                    column = int(user_input[COLUMN_INDEX])
                except ValueError as value_error:
                    print(value_error)
                    input("Press enter to continue")
                    continue

                try:
                    self.console_board.make_move(row, column, symbol)
                except ValueError as index_error:
                    print(index_error)
                    input("Press enter to continue")
                    continue
            else:
                row, column = self.ai.make_a_move()
                self.console_board.make_move(row, column, symbol)

            if self.console_board.check_game_state(row, column, symbol) != 111:
                self.print_final_state(row, column, symbol)
                game_is_running = False
                continue
            symbol = ConsoleUI.change_symbol(symbol)
