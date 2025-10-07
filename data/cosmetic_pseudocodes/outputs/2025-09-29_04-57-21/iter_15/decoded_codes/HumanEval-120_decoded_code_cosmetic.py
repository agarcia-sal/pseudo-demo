from typing import List


def maximum(array_of_integers: List[int], positive_integer_k: int) -> List[int]:
    if positive_integer_k == 0:
        return []

    array_of_integers.sort()

    start_index = len(array_of_integers) - positive_integer_k
    result_subset: List[int] = []

    current_index = start_index
    while current_index < len(array_of_integers):
        result_subset.append(array_of_integers[current_index])
        current_index += 1

    return result_subset