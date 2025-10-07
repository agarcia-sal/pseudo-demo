from typing import List

def add(list_of_integers: List[int]) -> int:
    total = 0
    # Indices in pseudocode start at 1, so adjust accordingly for Python (0-based)
    for idx in range(1, len(list_of_integers) + 1):
        if idx % 2 == 1 and list_of_integers[idx - 1] % 2 == 0:
            total += list_of_integers[idx - 1]
    return total