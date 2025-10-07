from typing import List

def search(list_of_integers: List[int]) -> int:
    max_val = max(list_of_integers) if list_of_integers else 0
    counts: List[int] = [0] * (max_val + 1)
    for current_val in list_of_integers:
        counts[current_val] += 1
    result = -1
    position = len(counts) - 1
    while position >= 1:
        freq = counts[position]
        if freq >= position:
            result = position
        position -= 1
    return result