from typing import List

def smallest_change(array_of_integers: List[int]) -> int:
    count: int = 0
    length: int = len(array_of_integers)
    half: int = length // 2
    # Compare symmetrical pairs from start and end, excluding middle if odd length
    for i in range(half):
        if array_of_integers[i] != array_of_integers[length - i - 1]:
            count += 1
    return count