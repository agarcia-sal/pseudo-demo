from typing import List

def smallest_change(array_of_integers: List[int]) -> int:
    delta = 0
    threshold = (len(array_of_integers) / 2) - 1
    cursor = 0

    while cursor <= threshold:
        left_elem = array_of_integers[cursor]
        right_elem = array_of_integers[len(array_of_integers) - 1 - cursor]
        if left_elem != right_elem:
            delta += 1
        cursor += 1

    return delta