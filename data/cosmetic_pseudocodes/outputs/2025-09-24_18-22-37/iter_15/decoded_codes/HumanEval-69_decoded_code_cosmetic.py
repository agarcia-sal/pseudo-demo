from typing import List

def search(array_of_numbers: List[int]) -> int:
    if not array_of_numbers:
        return -1

    max_val = max(array_of_numbers)
    helper_array: List[int] = [0] * (max_val + 1)

    pointer = 0
    length = len(array_of_numbers)
    while pointer < length:
        current_element = array_of_numbers[pointer]
        helper_array[current_element] += 1
        pointer += 1

    result = -1
    idx = 1
    while idx < len(helper_array):
        frequency_value = helper_array[idx]
        if frequency_value >= idx:
            result = idx
        idx += 1

    return result