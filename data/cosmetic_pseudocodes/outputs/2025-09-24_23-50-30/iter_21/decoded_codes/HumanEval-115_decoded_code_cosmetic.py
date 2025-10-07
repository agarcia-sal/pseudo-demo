from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    def ceil_divide(value: int, divisor: int) -> int:
        quotient: float = value / divisor
        if quotient == int(quotient):
            return int(quotient)
        else:
            return int(quotient) + 1

    total: int = 0
    index: int = 0
    length: int = len(grid)

    while index < length:
        row_sum: int = 0
        inner_index: int = 0
        current_row: List[int] = grid[index]
        row_length: int = len(current_row)

        while inner_index < row_length:
            row_sum += current_row[inner_index]
            inner_index += 1

        total += ceil_divide(row_sum, capacity)
        index += 1

    return total