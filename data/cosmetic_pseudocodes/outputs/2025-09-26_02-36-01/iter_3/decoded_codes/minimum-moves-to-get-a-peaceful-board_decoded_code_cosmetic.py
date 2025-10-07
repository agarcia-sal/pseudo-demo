class Solution:
    def minMoves(self, rooks):
        count = 0
        total_rooks = len(rooks)
        sorted_rows = []
        sorted_columns = []

        i = 0
        while i < total_rooks:
            sorted_rows.append(rooks[i])
            sorted_columns.append(rooks[i])
            i += 1

        sorted_rows.sort(key=lambda item: item[0])
        sorted_columns.sort(key=lambda elem: elem[1])

        moves_for_rows = 0
        k = 0
        while k < total_rooks:
            pos_diff = sorted_rows[k][0] - k
            if pos_diff < 0:
                pos_diff = -pos_diff
            moves_for_rows += pos_diff
            k += 1

        moves_for_cols = 0
        j = 0
        while j < total_rooks:
            col_diff = sorted_columns[j][1] - j
            if col_diff < 0:
                col_diff = -col_diff
            moves_for_cols += col_diff
            j += 1

        final_total = moves_for_rows + moves_for_cols
        return final_total