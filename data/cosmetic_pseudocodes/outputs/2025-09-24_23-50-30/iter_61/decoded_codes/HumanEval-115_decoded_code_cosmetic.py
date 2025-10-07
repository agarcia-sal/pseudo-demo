from typing import List


def max_fill(matrix: List[List[int]], limit: int) -> int:
    def helper(idx: int, acc: int) -> int:
        if idx < len(matrix):
            return helper(idx + 1, acc + sum(matrix[idx]))
        else:
            return acc

    total_sum = helper(0, 0)
    result = 0
    while total_sum > 0:
        total_sum -= limit
        result += 1

    return result