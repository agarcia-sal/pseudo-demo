from typing import List


def max_fill(grid: List[List[int]], capacity: int) -> int:
    def accumulate_rows(inputGrid: List[List[int]], idx: int, acc: int, outList: List[int]) -> List[int]:
        if idx >= len(inputGrid):
            return outList
        else:
            current_row = inputGrid[idx]

            def sum_elements(elements: List[int], pos: int, result: int) -> int:
                if pos >= len(elements):
                    return result
                else:
                    return sum_elements(elements, pos + 1, result + elements[pos])

            rowSum = sum_elements(current_row, 0, 0)
            return accumulate_rows(inputGrid, idx + 1, acc, outList + [rowSum])

    def ceiling_sum(values: List[int], pos: int, totalAcc: int) -> int:
        if pos >= len(values):
            return totalAcc
        else:
            val = values[pos]
            divided = val / capacity
            int_div = int(divided)
            # ceilVal is int_div + 1 if divided is not integer, else int_div
            ceilVal = int_div + 1 if divided != int_div else int_div
            return ceiling_sum(values, pos + 1, totalAcc + ceilVal)

    row_totals = accumulate_rows(grid, 0, 0, [])
    return ceiling_sum(row_totals, 0, 0)