from typing import List

def max_fill(matrix: List[List[int]], limit: int) -> int:
    total = 0
    for line in matrix:
        numerator = sum(line)
        quotient = numerator / limit
        count = int(quotient) if quotient == int(quotient) else int(quotient) + 1
        total += count
    return total