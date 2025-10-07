class Solution:
    def findPattern(self, board, pattern):
        total_rows = len(board)
        total_cols = len(board[0]) if total_rows > 0 else 0
        pat_rows = len(pattern)
        pat_cols = len(pattern[0]) if pat_rows > 0 else 0

        def matches(row_start, col_start):
            map_char_to_digit = {}
            map_digit_to_char = {}

            for iii in range(pat_rows):
                for jjj in range(pat_cols):
                    p_ch = pattern[iii][jjj]
                    b_dig = board[row_start + iii][col_start + jjj]

                    if '0' <= p_ch <= '9':
                        if int(p_ch) != b_dig:
                            return False
                    else:
                        if p_ch in map_char_to_digit:
                            if map_char_to_digit[p_ch] != b_dig:
                                return False
                        else:
                            if b_dig in map_digit_to_char:
                                return False
                            map_char_to_digit[p_ch] = b_dig
                            map_digit_to_char[b_dig] = p_ch
            return True

        res_r, res_c = -1, -1
        found_match = False

        row_idx = 0
        while row_idx <= total_rows - pat_rows:
            col_idx = 0
            while col_idx <= total_cols - pat_cols:
                if matches(row_idx, col_idx):
                    res_r, res_c = row_idx, col_idx
                    found_match = True
                    break
                col_idx += 1
            if found_match:
                break
            row_idx += 1

        return [res_r, res_c]