class Solution:
    def findPattern(self, board, pattern):
        total_rows = len(board)
        total_cols = len(board[0]) if total_rows > 0 else 0
        pat_rows = len(pattern)
        pat_cols = len(pattern[0]) if pat_rows > 0 else 0

        def matches(row_x, col_x):
            map_char_to_digit = {}
            map_digit_to_char = {}

            def check_row(i):
                if i == pat_rows:
                    return True

                def check_col(j):
                    if j == pat_cols:
                        return check_row(i + 1)

                    char_p = pattern[i][j]
                    digit_b = board[row_x + i][col_x + j]

                    if '0' <= char_p <= '9':
                        if int(char_p) != digit_b:
                            return False
                        else:
                            return check_col(j + 1)
                    else:
                        if char_p in map_char_to_digit:
                            if map_char_to_digit[char_p] != digit_b:
                                return False
                            else:
                                return check_col(j + 1)
                        else:
                            if digit_b in map_digit_to_char:
                                return False
                            else:
                                map_char_to_digit[char_p] = digit_b
                                map_digit_to_char[digit_b] = char_p
                                return check_col(j + 1)

                return check_col(0)

            return check_row(0)

        pos_row = 0
        while pos_row <= total_rows - pat_rows:
            pos_col = 0
            while pos_col <= total_cols - pat_cols:
                if matches(pos_row, pos_col):
                    return [pos_row, pos_col]
                pos_col += 1
            pos_row += 1

        return [-1, -1]