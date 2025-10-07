from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    result_list: List[int] = []
    idx: int = 0
    while idx < len(grid):
        temp_row: List[int] = grid[idx]
        accum: int = 0
        jdx: int = 0
        while jdx < len(temp_row):
            accum += temp_row[jdx]
            jdx += 1
        division: float = accum / capacity
        ceiling_value: int = int(division)
        if ceiling_value != division:
            ceiling_value = ceiling_value + 1
        result_list.append(ceiling_value)
        idx += 1
    total: int = 0
    kdx: int = 0
    while kdx < len(result_list):
        total += result_list[kdx]
        kdx += 1
    return total