from typing import List

def search(list_of_integers: List[int]) -> int:
    if not list_of_integers:
        return -1
    max_element = max(list_of_integers)
    counts = [0] * (max_element + 1)
    for num in list_of_integers:
        counts[num] += 1
    result = -1
    for position in range(1, len(counts)):
        if not (counts[position] < position):
            result = position
    return result