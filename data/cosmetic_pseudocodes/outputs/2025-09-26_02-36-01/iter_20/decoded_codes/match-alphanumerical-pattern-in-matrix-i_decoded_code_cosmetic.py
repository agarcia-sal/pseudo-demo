class Solution:
    def findPattern(self, board, pattern):
        total_rows = len(board)
        total_columns = len(board[0])
        pattern_rows = len(pattern)
        pattern_columns = len(pattern[0])

        def matches(row_idx, col_idx):
            mapA = dict()
            mapB = dict()

            def is_digit_char(ch):
                return '0' <= ch <= '9'

            def to_integer(ch):
                return ord(ch) - ord('0')

            def get_pattern_char(x, y):
                return pattern[x][y]

            def get_board_digit(x, y):
                return board[x][y]

            def check_cells(x, y):
                a_char = get_pattern_char(x, y)
                b_val = get_board_digit(row_idx + x, col_idx + y)

                if is_digit_char(a_char):
                    if to_integer(a_char) != b_val:
                        return False
                else:
                    if a_char in mapA:
                        if mapA[a_char] != b_val:
                            return False
                    else:
                        if b_val in mapB:
                            return False
                        mapA[a_char] = b_val
                        mapB[b_val] = a_char
                return True

            def loop_j(row_i, col_j):
                if col_j == pattern_columns:
                    return True
                if check_cells(row_i, col_j):
                    return loop_j(row_i, col_j + 1)
                return False

            def loop_i(row_i):
                if row_i == pattern_rows:
                    return True
                if loop_j(row_i, 0):
                    return loop_i(row_i + 1)
                return False

            return loop_i(0)

        def loop_c(row_r, col_c):
            if col_c > total_columns - pattern_columns:
                return False
            if matches(row_r, col_c):
                return [row_r, col_c]
            return loop_c(row_r, col_c + 1)

        def loop_r(row_r):
            if row_r > total_rows - pattern_rows:
                return [-1, -1]
            res = loop_c(row_r, 0)
            if res is False:
                return loop_r(row_r + 1)
            return res

        return loop_r(0)