class Solution:
    def findPattern(self, board, pattern):
        ZERO = 0
        ONE = 1

        total_rows = len(board)
        total_cols = len(board[ZERO])
        pattern_rows = len(pattern)
        pattern_cols = len(pattern[ZERO])

        def matches(row_start, col_start):
            char_to_digit_map = {}
            digit_to_char_map = {}

            i = ZERO
            while i < pattern_rows:
                j = ZERO
                while j < pattern_cols:
                    pattern_char = pattern[i][j]
                    board_digit = board[row_start + i][col_start + j]

                    if '0' <= pattern_char <= '9':
                        if int(pattern_char) != board_digit:
                            return False
                    else:
                        if pattern_char in char_to_digit_map:
                            if char_to_digit_map[pattern_char] != board_digit:
                                return False
                        else:
                            if board_digit in digit_to_char_map:
                                return False
                            else:
                                char_to_digit_map[pattern_char] = board_digit
                                digit_to_char_map[board_digit] = pattern_char

                    j += ONE
                i += ONE

            return True

        row_index = ZERO
        while row_index <= total_rows - pattern_rows:
            col_index = ZERO
            while col_index <= total_cols - pattern_cols:
                if matches(row_index, col_index):
                    return [row_index, col_index]
                col_index += ONE
            row_index += ONE

        return [-1, -1]