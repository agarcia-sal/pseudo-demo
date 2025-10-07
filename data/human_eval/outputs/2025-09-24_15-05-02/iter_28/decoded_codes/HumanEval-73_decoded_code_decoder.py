from typing import List

def smallest_change(array: List[int]) -> int:
    changes_needed = 0
    n = len(array)
    for index in range(n // 2):
        if array[index] != array[n - index - 1]:
            changes_needed += 1
    return changes_needed