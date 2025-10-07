class Solution:
    def minMoves(self, rooks):
        total_rooks = len(rooks)

        sorted_by_row = sorted(rooks, key=lambda element: element[0])
        sorted_by_col = sorted(rooks, key=lambda element: element[1])

        moves_rows = 0
        idx_row = 0
        while idx_row < total_rooks:
            current_row_pos = sorted_by_row[idx_row][0]
            displacement_row = current_row_pos

            if displacement_row < idx_row:
                displacement_row = idx_row - displacement_row
            else:
                displacement_row = displacement_row - idx_row

            moves_rows += displacement_row
            idx_row += 1

        moves_columns = 0
        idx_col = 0
        while idx_col < total_rooks:
            current_col_pos = sorted_by_col[idx_col][1]
            displacement_col = current_col_pos

            if displacement_col < idx_col:
                displacement_col = idx_col - displacement_col
            else:
                displacement_col = displacement_col - idx_col

            moves_columns += displacement_col
            idx_col += 1

        final_moves = moves_rows + moves_columns
        return final_moves