from typing import List

def maximum(array_of_integers: List[int], positive_integer_k: int) -> List[int]:
    temp_collection: List[int] = []
    array_length: int = len(array_of_integers)

    if positive_integer_k == 0:
        return temp_collection

    array_of_integers.sort()
    start_position: int = array_length - positive_integer_k
    current_index: int = start_position

    while current_index < array_length:
        temp_collection.append(array_of_integers[current_index])
        current_index += 1

    return temp_collection