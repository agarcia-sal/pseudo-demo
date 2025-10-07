from typing import List

def sort_third(l: List[int]) -> List[int]:
    l = l.copy()
    indices_divisible_by_three = [i for i in range(len(l)) if i % 3 == 0]
    elements_at_indices_divisible_by_three = [l[i] for i in indices_divisible_by_three]
    elements_at_indices_divisible_by_three.sort()
    for i, sorted_value in zip(indices_divisible_by_three, elements_at_indices_divisible_by_three):
        l[i] = sorted_value
    return l