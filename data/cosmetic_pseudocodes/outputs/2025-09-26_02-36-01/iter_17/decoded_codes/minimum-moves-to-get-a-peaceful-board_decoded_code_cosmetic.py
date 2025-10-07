from typing import List, Tuple

class Solution:
    def minMoves(self, rooks: List[Tuple[int, int]]) -> int:
        total_rooks = len(rooks)
        ordered_by_row = []
        ordered_by_col = []

        # Sort by row using selection sort logic as in pseudocode
        temp_list = rooks.copy()
        while temp_list:
            min_idx = 0
            for j in range(1, len(temp_list)):
                if temp_list[j][0] < temp_list[min_idx][0]:
                    min_idx = j
            ordered_by_row.append(temp_list[min_idx])
            temp_list.pop(min_idx)

        # Sort by column using selection sort logic as in pseudocode
        temp_list = rooks.copy()
        while temp_list:
            min_idx = 0
            for k in range(1, len(temp_list)):
                if temp_list[k][1] < temp_list[min_idx][1]:
                    min_idx = k
            ordered_by_col.append(temp_list[min_idx])
            temp_list.pop(min_idx)

        # Calculate required moves for rows
        r = 0
        hm = 0
        while True:
            if r >= total_rooks:
                break
            delta_row = ordered_by_row[r][0]
            diff_row = delta_row - r if delta_row >= r else r - delta_row
            hm += diff_row
            r += 1

        # Calculate required moves for columns
        s = 0
        tm = 0
        while True:
            if s >= total_rooks:
                break
            delta_col = ordered_by_col[s][1]
            diff_col = delta_col - s if delta_col >= s else s - delta_col
            tm += diff_col
            s += 1

        return hm + tm