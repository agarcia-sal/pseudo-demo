class Solution:
    def minMoves(self, rooks):
        total_rows = 0
        total_cols = 0
        length_rooks = len(rooks)

        # Sort rooks by row using built-in sorted for efficiency
        sorted_by_row = sorted(rooks, key=lambda x: x[0])
        # Sort rooks by column using built-in sorted for efficiency
        sorted_by_col = sorted(rooks, key=lambda x: x[1])

        for idx in range(length_rooks):
            delta_row = abs(sorted_by_row[idx][0] - idx)
            total_rows += delta_row

        for idx in range(length_rooks):
            delta_col = abs(sorted_by_col[idx][1] - idx)
            total_cols += delta_col

        result = total_rows + total_cols
        return result