from typing import List


def maximum(array_of_integers: List[int], positive_integer_k: int) -> List[int]:
    if positive_integer_k == 0:
        return []
    # Bubble sort ascending
    n = len(array_of_integers)
    for temp_index in range(n - 1):
        for inner_index in range(n - 1 - temp_index):
            if array_of_integers[inner_index] > array_of_integers[inner_index + 1]:
                array_of_integers[inner_index], array_of_integers[inner_index + 1] = (
                    array_of_integers[inner_index + 1],
                    array_of_integers[inner_index],
                )

    start_slice_index = n - positive_integer_k
    return array_of_integers[start_slice_index:]