from typing import Sequence

def smallest_change(collection_of_integers: Sequence[int]) -> int:
    result: int = 0
    position: int = 0
    midpoint: int = len(collection_of_integers) // 2
    while position < midpoint:
        first_elem: int = collection_of_integers[position]
        second_elem: int = collection_of_integers[len(collection_of_integers) - position - 1]
        if first_elem != second_elem:
            result += 1
        position += 1
    return result