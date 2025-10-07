from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    # Ceiling division via integer arithmetic without math.ceil
    ceiling_div = lambda x: (x + capacity - 1) // capacity

    # Sum each row, then map ceiling_div over those sums, then sum the results
    return sum(ceiling_div(sum(row)) for row in grid)