from typing import List

def solution(list_of_integers: List[int]) -> int:
    total = 0
    # Iterate over 1-based odd positions, which are even indices in zero-based Python
    for position in range(1, len(list_of_integers), 2):
        if list_of_integers[position] % 2 != 0:
            total += list_of_integers[position]
    return total