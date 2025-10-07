from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    def helper(rowset: List[List[int]], acc: int) -> int:
        if not rowset:
            return acc
        head, tail = rowset[0], rowset[1:]
        partial_sum = sum(head) / capacity
        increment = int(partial_sum) if partial_sum == int(partial_sum) else int(partial_sum) + 1
        return helper(tail, acc + increment)
    return helper(grid, 0)