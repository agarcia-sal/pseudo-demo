from typing import List, Optional, Tuple

def find_closest_elements(numbers: List[int]) -> Optional[Tuple[int, int]]:
    pair_result: Optional[Tuple[int, int]] = None
    smallest_gap: Optional[int] = None
    length = len(numbers)
    for i in range(length):
        for j in range(length):
            if i != j:
                dist = abs(numbers[i] - numbers[j])
                if smallest_gap is None or dist < smallest_gap:
                    smallest_gap = dist
                    if numbers[i] < numbers[j]:
                        pair_result = (numbers[i], numbers[j])
                    else:
                        pair_result = (numbers[j], numbers[i])
    return pair_result