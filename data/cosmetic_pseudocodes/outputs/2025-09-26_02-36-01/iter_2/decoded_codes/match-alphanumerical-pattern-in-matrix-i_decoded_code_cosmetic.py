class Solution:
    def findPattern(self, board, pattern):
        total_rows = len(board)
        total_cols = len(board[0])
        pattern_rows = len(pattern)
        pattern_cols = len(pattern[0])

        def matches(row_start, col_start):
            map_char_to_digit = {}
            map_digit_to_char = {}

            for row_idx in range(pattern_rows):
                for col_idx in range(pattern_cols):
                    current_char = pattern[row_idx][col_idx]
                    current_digit = board[row_start + row_idx][col_start + col_idx]

                    if '0' <= current_char <= '9':
                        expected_digit = int(current_char)
                        if expected_digit != current_digit:
                            return False
                    else:
                        if current_char in map_char_to_digit:
                            if map_char_to_digit[current_char] != current_digit:
                                return False
                        else:
                            if current_digit in map_digit_to_char:
                                return False
                            map_char_to_digit[current_char] = current_digit
                            map_digit_to_char[current_digit] = current_char
            return True

        for r_index in range(total_rows - pattern_rows + 1):
            for c_index in range(total_cols - pattern_cols + 1):
                if matches(r_index, c_index):
                    return [r_index, c_index]

        return [-1, -1]