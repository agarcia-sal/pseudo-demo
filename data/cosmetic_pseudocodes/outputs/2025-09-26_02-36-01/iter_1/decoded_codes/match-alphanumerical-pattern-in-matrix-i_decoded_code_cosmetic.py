class Solution:
    def findPattern(self, board, pattern):
        total_rows = len(board)
        total_cols = len(board[0])
        pattern_rows = len(pattern)
        pattern_cols = len(pattern[0])

        def matches(row_start, col_start):
            char_to_digit_map = {}
            digit_to_char_map = {}

            for row_offset in range(pattern_rows):
                for col_offset in range(pattern_cols):
                    pattern_char = pattern[row_offset][col_offset]
                    board_digit = board[row_start + row_offset][col_start + col_offset]

                    if pattern_char.isdigit():
                        if int(pattern_char) != board_digit:
                            return False
                    else:
                        if pattern_char in char_to_digit_map:
                            if char_to_digit_map[pattern_char] != board_digit:
                                return False
                        else:
                            if board_digit in digit_to_char_map:
                                return False
                            char_to_digit_map[pattern_char] = board_digit
                            digit_to_char_map[board_digit] = pattern_char
            return True

        for row_index in range(total_rows - pattern_rows + 1):
            for col_index in range(total_cols - pattern_cols + 1):
                if matches(row_index, col_index):
                    return [row_index, col_index]

        return [-1, -1]