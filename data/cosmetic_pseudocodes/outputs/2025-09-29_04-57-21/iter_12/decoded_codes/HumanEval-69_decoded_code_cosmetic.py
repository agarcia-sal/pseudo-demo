from typing import List

def search(list_of_integers: List[int]) -> int:
    highest_number: int = 0
    iterator_pos: int = 0
    while iterator_pos < len(list_of_integers):
        current_element = list_of_integers[iterator_pos]
        if current_element > highest_number:
            highest_number = current_element
        iterator_pos += 1

    counts: List[int] = [0] * (highest_number + 1)

    pos: int = 0
    while pos < len(list_of_integers):
        num = list_of_integers[pos]
        counts[num] += 1
        pos += 1

    candidate: int = -1
    idx: int = 1
    while idx <= highest_number:
        if not (counts[idx] < idx):
            candidate = idx
        idx += 1

    return candidate