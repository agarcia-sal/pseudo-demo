from typing import List

def smallest_change(array_of_integers: List[int]) -> int:
    def count_pairs(m: int, n: int) -> int:
        if m >= n:
            return 0
        return (array_of_integers[m] != array_of_integers[n]) + count_pairs(m + 1, n - 1)
    return count_pairs(0, len(array_of_integers) - 1)