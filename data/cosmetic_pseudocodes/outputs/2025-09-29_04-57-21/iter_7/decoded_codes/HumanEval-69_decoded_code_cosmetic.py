from typing import List

def search(list_of_integers: List[int]) -> int:
    if not list_of_integers:
        return -1  # no elements to process

    max_element = max(list_of_integers)
    occurrence_counts: List[int] = [0] * (max_element + 1)

    pointer: int = 0
    length: int = len(list_of_integers)
    while pointer < length:
        current_value = list_of_integers[pointer]
        occurrence_counts[current_value] += 1
        pointer += 1

    result: int = -1
    counter: int = 1
    while counter < len(occurrence_counts):
        if not (occurrence_counts[counter] < counter):
            result = counter
        counter += 1

    return result