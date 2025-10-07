from typing import List

def search(array_of_numbers: List[int]) -> int:
    if not array_of_numbers:
        return -1

    size_of_frequencies: int = max(array_of_numbers) + 1
    count_array: List[int] = [0] * size_of_frequencies

    cursor: int = 0
    while cursor < len(array_of_numbers):
        current_val: int = array_of_numbers[cursor]
        old_count: int = count_array[current_val]
        new_count: int = old_count + 1
        count_array[current_val] = new_count
        cursor += 1

    result_flag: int = -1
    pos: int = 1
    while pos < len(count_array):
        threshold: int = count_array[pos]
        if threshold >= pos:
            result_flag = pos
        pos += 1

    return result_flag