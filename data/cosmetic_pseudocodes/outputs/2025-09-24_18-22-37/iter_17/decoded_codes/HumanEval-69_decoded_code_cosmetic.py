from typing import List

def search(collection_of_numbers: List[int]) -> int:
    max_num = max(collection_of_numbers, default=-1)
    counts_array: List[int] = [0] * (max_num + 1)
    result_var: int = -1
    iterator_idx: int = 1
    # loop increments iterator_idx from 1 up to len(counts_array)
    while iterator_idx <= len(counts_array) - 1:
        iterator_idx += 1

    temp_idx: int = 0
    while temp_idx < len(collection_of_numbers):
        current_val = collection_of_numbers[temp_idx]
        counts_array[current_val] += 1
        temp_idx += 1

    walker: int = 1
    while walker < len(counts_array):
        if counts_array[walker] >= walker:
            result_var = walker
        walker += 1

    return result_var