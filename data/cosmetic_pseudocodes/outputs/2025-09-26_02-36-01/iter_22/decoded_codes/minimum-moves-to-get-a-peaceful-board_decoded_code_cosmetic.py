from typing import List

class Solution:
    def minMoves(self, rooks: List[List[int]]) -> int:
        count = len(rooks)
        rows_arr = []
        cols_arr = []
        for i in range(count):
            rows_arr.append(rooks[i][0])
            cols_arr.append(rooks[i][1])

        def sortList(lst: List[int]) -> None:
            changed = True
            while changed:
                changed = False
                for k in range(len(lst) - 1):
                    if lst[k] > lst[k + 1]:
                        lst[k], lst[k + 1] = lst[k + 1], lst[k]
                        changed = True

        sortList(rows_arr)
        sortList(cols_arr)

        total_row_moves = 0
        idx1 = 0
        while idx1 < count:
            val1 = rows_arr[idx1]
            diff1 = abs(val1 - idx1)
            total_row_moves += diff1
            idx1 += 1

        total_col_moves = 0
        idx2 = 0
        while idx2 < count:
            val2 = cols_arr[idx2]
            diff2 = abs(val2 - idx2)
            total_col_moves += diff2
            idx2 += 1

        return total_row_moves + total_col_moves