class Solution:
    def minMoves(self, rooks):
        sorted_by_row = rooks[:]
        sorted_by_row.sort(key=lambda x: x[0])

        sorted_by_col = rooks[:]
        sorted_by_col.sort(key=lambda x: x[1])

        accum_row_moves = 0
        for i, (r, _) in enumerate(sorted_by_row):
            accum_row_moves += abs(r - i)

        accum_col_moves = 0
        for i, (_, c) in enumerate(sorted_by_col):
            accum_col_moves += abs(c - i)

        return accum_row_moves + accum_col_moves