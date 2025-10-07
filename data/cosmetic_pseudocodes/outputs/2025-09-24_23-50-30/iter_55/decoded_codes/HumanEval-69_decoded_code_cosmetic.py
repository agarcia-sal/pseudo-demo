from typing import List

def search(list_of_integers: List[int]) -> int:
    if not list_of_integers:
        return -1  # early return for empty list to avoid max() error

    max_element = max(list_of_integers)
    frequency_array: List[int] = [0] * (max_element + 1)

    def increment_frequency(current_list: List[int], idx: int) -> None:
        if not current_list:
            return
        head_element = current_list[0]
        tail_elements = current_list[1:]
        frequency_array[head_element] += 1
        increment_frequency(tail_elements, idx + 1)

    increment_frequency(list_of_integers, 0)

    result_value: int = -1

    def find_answer(index: int) -> None:
        nonlocal result_value
        if index > len(frequency_array) - 1:
            return
        if frequency_array[index] >= index:
            result_value = index
        find_answer(index + 1)

    find_answer(1)

    return result_value