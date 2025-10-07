class Solution:
    def findPattern(self, board, pattern):
        rows = len(board)
        cols = len(board[0]) if rows > 0 else 0
        p_rows = len(pattern)
        p_cols = len(pattern[0]) if p_rows > 0 else 0

        def matches(r, c):
            char_to_digit = {}
            digit_to_char = {}

            for i in range(p_rows):
                for j in range(p_cols):
                    p_char = pattern[i][j]
                    b_digit = board[r + i][c + j]

                    if p_char.isdigit():
                        if int(p_char) != b_digit:
                            return False
                    else:
                        if p_char in char_to_digit:
                            if char_to_digit[p_char] != b_digit:
                                return False
                        else:
                            if b_digit in digit_to_char:
                                return False
                            char_to_digit[p_char] = b_digit
                            digit_to_char[b_digit] = p_char
            return True

        for r in range(rows - p_rows + 1):
            for c in range(cols - p_cols + 1):
                if matches(r, c):
                    return [r, c]

        return [-1, -1]