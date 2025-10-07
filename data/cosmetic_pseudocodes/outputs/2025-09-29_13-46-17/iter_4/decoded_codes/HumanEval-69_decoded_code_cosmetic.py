from typing import List

def search(input_array: List[int]) -> int:
    freq_array: List[int] = [0] * (1 + max(input_array, default=-1))

    def increment_frequency(position: int) -> None:
        if position == len(input_array):
            return
        freq_array[input_array[position]] += 1
        increment_frequency(position + 1)

    increment_frequency(0)

    result_value: int = -1

    def find_answer(current_index: int) -> None:
        nonlocal result_value
        if current_index == len(freq_array):
            return
        if not (freq_array[current_index] < current_index):
            result_value = current_index
        find_answer(current_index + 1)

    find_answer(1)

    return result_value