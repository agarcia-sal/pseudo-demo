from typing import List, Optional, Tuple


def find_closest_elements(numbers: List[int]) -> Optional[Tuple[int, int]]:
    pair_with_min_diff: Optional[Tuple[int, int]] = None
    smallest_gap: float = float('inf')

    length = len(numbers)
    for i in range(length):
        for j in range(length):
            if i != j:
                diff = abs(numbers[i] - numbers[j])
                if diff < smallest_gap:
                    smallest_gap = diff
                    pair_with_min_diff = tuple(sorted((numbers[i], numbers[j])))

    return pair_with_min_diff