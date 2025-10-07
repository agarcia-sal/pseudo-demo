from typing import List

def smallest_change(array: List[int]) -> int:
    if not array:
        return 0  # Empty array requires no changes
    n: int = len(array)
    ans: int = 0
    half_length: int = n // 2
    for index in range(half_length):
        if array[index] != array[n - index - 1]:
            ans += 1
    return ans