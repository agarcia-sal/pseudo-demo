from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    total_cells: int = 0
    index: int = 0
    while index < len(grid):
        accumulator: int = 0
        cell_index: int = 0
        row_data: List[int] = grid[index]
        while cell_index < len(row_data):
            accumulator += row_data[cell_index]
            cell_index += 1
        total_cells += (accumulator + capacity - 1) // capacity
        index += 1
    return total_cells