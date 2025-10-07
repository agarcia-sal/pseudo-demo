from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    def helper(accumulator: int, index: int) -> int:
        if index == len(grid):
            return accumulator
        def row_sum(rowlist: List[int], pointer: int, total: int) -> int:
            if pointer == len(rowlist):
                return total
            else:
                return row_sum(rowlist, pointer + 1, total + rowlist[pointer])
        current_row_sum = row_sum(grid[index], 0, 0)
        division_result = current_row_sum / capacity
        ceil_value = int(division_result) if division_result == int(division_result) else int(division_result) + 1
        return helper(accumulator + ceil_value, index + 1)
    return helper(0, 0)