from typing import List

def search(list_of_integers: List[int]) -> int:
    if not list_of_integers:
        return -1
    max_val = max(list_of_integers)
    counts: List[int] = [0] * (max_val + 1)
    iterator = 0
    while iterator < len(list_of_integers):
        current_value = list_of_integers[iterator]
        counts[current_value] += 1
        iterator += 1
    result = -1
    position = 1
    while position < len(counts):
        if not (counts[position] < position):
            result = position
        position += 1
    return result