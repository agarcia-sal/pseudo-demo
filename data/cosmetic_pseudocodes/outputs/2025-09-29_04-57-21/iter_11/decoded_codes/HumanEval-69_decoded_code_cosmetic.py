from typing import List

def search(list_of_integers: List[int]) -> int:
    if not list_of_integers:
        return -1
    max_element = max(list_of_integers)
    counts = [0] * (max_element + 1)
    iterator = 0
    while iterator < len(list_of_integers):
        current_element = list_of_integers[iterator]
        counts[current_element] += 1
        iterator += 1
    result_value = -1
    position = 1
    while position < len(counts):
        if not (counts[position] < position):
            result_value = position
        position += 1
    return result_value