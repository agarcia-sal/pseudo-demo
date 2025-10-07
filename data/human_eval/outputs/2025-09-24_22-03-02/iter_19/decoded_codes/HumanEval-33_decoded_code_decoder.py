from typing import List, Any

def sort_third(l: list) -> list:
    l = list(l)
    indices_divisible_by_three: List[int] = []
    values_at_divisible_indices: List[Any] = []
    i = 0
    while i < len(l):
        if i % 3 == 0:
            indices_divisible_by_three.append(i)
            values_at_divisible_indices.append(l[i])
        i += 1
    values_at_divisible_indices = sorted(values_at_divisible_indices)
    j = 0
    while j < len(indices_divisible_by_three):
        l[indices_divisible_by_three[j]] = values_at_divisible_indices[j]
        j += 1
    return l