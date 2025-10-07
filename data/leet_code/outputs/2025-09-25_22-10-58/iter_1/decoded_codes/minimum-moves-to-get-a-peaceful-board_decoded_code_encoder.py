class Solution:
    def minMoves(self, rooks: list[list[int]]) -> int:
        n = len(rooks)
        rooks_by_row = sorted(rooks, key=lambda x: x[0])
        rooks_by_col = sorted(rooks, key=lambda x: x[1])

        row_moves = 0
        for i in range(n):
            row_moves += abs(rooks_by_row[i][0] - i)

        col_moves = 0
        for i in range(n):
            col_moves += abs(rooks_by_col[i][1] - i)

        return row_moves + col_moves