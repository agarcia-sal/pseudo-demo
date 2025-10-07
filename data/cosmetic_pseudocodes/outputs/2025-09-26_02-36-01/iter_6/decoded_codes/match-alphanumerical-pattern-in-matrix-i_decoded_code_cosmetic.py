class Solution:
    def findPattern(self, board, pattern):
        total_rows = len(board)
        total_cols = len(board[0])
        pattern_rows = len(pattern)
        pattern_cols = len(pattern[0])

        def matches(row_idx, col_idx):
            map_char_to_digit = {}
            map_digit_to_char = {}

            def recursive_traverse(i, j):
                if i > pattern_rows - 1:
                    return True
                if j > pattern_cols - 1:
                    return recursive_traverse(i + 1, 0)

                pattern_char = pattern[i][j]
                board_digit = board[row_idx + i][col_idx + j]

                if '0' <= pattern_char <= '9':
                    if int(pattern_char) != board_digit:
                        return False
                    else:
                        return recursive_traverse(i, j + 1)
                else:
                    if pattern_char in map_char_to_digit:
                        if map_char_to_digit[pattern_char] != board_digit:
                            return False
                        else:
                            return recursive_traverse(i, j + 1)
                    else:
                        if board_digit in map_digit_to_char:
                            return False
                        else:
                            map_char_to_digit[pattern_char] = board_digit
                            map_digit_to_char[board_digit] = pattern_char
                            return recursive_traverse(i, j + 1)

            return recursive_traverse(0, 0)

        row_cursor = 0
        while row_cursor <= total_rows - pattern_rows:
            col_cursor = 0
            while col_cursor <= total_cols - pattern_cols:
                if matches(row_cursor, col_cursor):
                    return [row_cursor, col_cursor]
                col_cursor += 1
            row_cursor += 1

        return [-1, -1]