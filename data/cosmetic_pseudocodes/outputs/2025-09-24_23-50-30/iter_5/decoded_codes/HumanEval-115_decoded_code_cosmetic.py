from typing import List


def max_fill(grid: List[List[int]], capacity: int) -> int:
    result: int = 0
    index: int = 0
    length: int = len(grid)

    while index < length:
        current_row: List[int] = grid[index]
        row_total: int = 0
        pos: int = 0
        row_length: int = len(current_row)

        while True:
            if pos >= row_length:
                break
            row_total += current_row[pos]
            pos += 1

        division: float = row_total / capacity
        # Determine the ceiling of the division without math.ceil to match pseudocode logic
        if division == int(division):
            ceil_value: int = int(division)
        else:
            ceil_value: int = int(division) + 1

        result += ceil_value
        index += 1

    return result