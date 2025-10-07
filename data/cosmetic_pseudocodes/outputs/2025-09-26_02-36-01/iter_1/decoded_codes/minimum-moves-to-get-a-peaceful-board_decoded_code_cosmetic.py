class Solution:
    def minMoves(self, rooks):
        count = len(rooks)
        sorted_rows = sorted(rooks, key=lambda x: x[0])
        sorted_columns = sorted(rooks, key=lambda x: x[1])

        total_row_moves = 0
        for i in range(count):
            total_row_moves += abs(sorted_rows[i][0] - i)

        total_column_moves = 0
        for j in range(count):
            total_column_moves += abs(sorted_columns[j][1] - j)

        return total_row_moves + total_column_moves