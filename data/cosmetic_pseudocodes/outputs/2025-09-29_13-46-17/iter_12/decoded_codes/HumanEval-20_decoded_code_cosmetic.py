from typing import List, Optional

def find_closest_elements(list_of_numbers: List[int]) -> Optional[List[int]]:
    closest_pair: Optional[List[int]] = None
    min_diff: Optional[int] = None
    n: int = len(list_of_numbers)
    for i in range(n):
        num_i: int = list_of_numbers[i]
        for j in range(n):
            num_j: int = list_of_numbers[j]
            if i != j:
                diff: int = abs(num_i - num_j)
                if min_diff is None:
                    min_diff = diff
                    closest_pair = sorted([num_i, num_j])
                else:
                    if diff < min_diff:
                        min_diff = diff
                        closest_pair = sorted([num_i, num_j])
    return closest_pair