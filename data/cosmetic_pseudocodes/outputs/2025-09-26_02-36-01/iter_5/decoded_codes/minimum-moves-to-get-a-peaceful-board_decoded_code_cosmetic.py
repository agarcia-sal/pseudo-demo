class Solution:
    def minMoves(self, rooks):
        total_rooks = len(rooks)
        sorted_rows = sorted(rooks, key=lambda x: x[0])
        sorted_cols = sorted(rooks, key=lambda y: y[1])

        def accumulateRowMoves(i_current, acc):
            if i_current == total_rooks:
                return acc
            pos_diff = sorted_rows[i_current][0]
            dist_calc = i_current
            abs_diff_val = pos_diff - dist_calc
            if abs_diff_val < 0:
                abs_diff_val = -abs_diff_val
            return accumulateRowMoves(i_current + 1, acc + abs_diff_val)

        sum_row_moves = accumulateRowMoves(0, 0)

        def accumulateColMoves(j_current, acc_col):
            if j_current == total_rooks:
                return acc_col
            col_pos = sorted_cols[j_current][1]
            index_ref = j_current
            abs_diff_col = col_pos - index_ref
            if abs_diff_col < 0:
                abs_diff_col = -abs_diff_col
            return accumulateColMoves(j_current + 1, acc_col + abs_diff_col)

        sum_col_moves = accumulateColMoves(0, 0)

        final_result = sum_row_moves + sum_col_moves
        return final_result