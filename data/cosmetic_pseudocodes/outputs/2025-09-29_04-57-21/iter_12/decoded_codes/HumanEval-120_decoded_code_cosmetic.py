from typing import List


def sortNonDecreasing(input_array: List[int]) -> None:
    input_array.sort()  # In-place sort in non-decreasing order


def maximum(array_of_integers: List[int], positive_integer_k: int) -> List[int]:
    if positive_integer_k == 0:
        return []

    sortNonDecreasing(array_of_integers)

    start_index: int = len(array_of_integers) - positive_integer_k
    result: List[int] = []

    current_pos: int = start_index
    while current_pos < len(array_of_integers):
        result.append(array_of_integers[current_pos])
        current_pos += 1

    return result