class Solution:
    def minMoves(self, rooks):
        total_rooks = 0
        iterator_rooks = rooks
        while total_rooks < len(iterator_rooks):
            total_rooks += 1

        def sortByFirstElement(lst):
            def insertSorted(accum, item):
                if len(accum) == 0:
                    return [item]
                else:
                    i = 0
                    while i < len(accum) and accum[i][0] <= item[0]:
                        i += 1
                    return accum[:i] + [item] + accum[i:]
            sorted_list = []
            j = 0
            while j < len(lst):
                sorted_list = insertSorted(sorted_list, lst[j])
                j += 1
            return sorted_list

        def sortBySecondElement(lst):
            def insertSorted(accum, item):
                if len(accum) == 0:
                    return [item]
                else:
                    k = 0
                    while k < len(accum) and accum[k][1] <= item[1]:
                        k += 1
                    return accum[:k] + [item] + accum[k:]
            sorted_list = []
            m = 0
            while m < len(lst):
                sorted_list = insertSorted(sorted_list, lst[m])
                m += 1
            return sorted_list

        ordered_by_row = sortByFirstElement(iterator_rooks)
        ordered_by_col = sortBySecondElement(iterator_rooks)

        def absVal(x):
            if x < 0:
                return -x
            else:
                return x

        acc_row_moves = 0
        p = 0
        while True:
            if not (p < total_rooks):
                break
            delta = ordered_by_row[p][0] + (-1 * p)
            abs_delta = absVal(delta)
            acc_row_moves += abs_delta
            p += 1

        aggregate_col_moves = 0
        q = 0
        while True:
            if not (q < total_rooks):
                break
            diff_val = ordered_by_col[q][1] + (-1 * q)
            abs_diff_val = absVal(diff_val)
            aggregate_col_moves += abs_diff_val
            q += 1

        return acc_row_moves + aggregate_col_moves