from typing import List


def max_fill(grid: List[List[int]], capacity: int) -> int:
    def sum_list(numbers: List[int]) -> int:
        total: int = 0
        for n in numbers:
            total += n
        return total

    def ceiling_division(value: int, divisor: int) -> int:
        if value - divisor * (value // divisor) > 0:
            return (value // divisor) + 1
        else:
            return value // divisor

    def helper(rows: List[List[int]], index: int, acc: int) -> int:
        if index >= len(rows):
            return acc
        row_sum = sum_list(rows[index])
        ceil_val = ceiling_division(row_sum, capacity)
        return helper(rows, index + 1, acc + ceil_val)

    return helper(grid, 0, 0)