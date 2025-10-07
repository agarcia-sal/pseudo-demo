from typing import List

def search(input_sequence: List[int]) -> int:
    max_element = max(input_sequence, default=0)
    freq_array: List[int] = [0] * (max_element + 1)  # +1 as per pseudocode

    def increment_index(position: int, limit: int) -> None:
        if position > limit:
            return
        freq_array[position] += 1
        increment_index(position + 1, limit)

    def loop_over_elements(iterator: int, end: int) -> None:
        if iterator > end:
            return
        increment_index(input_sequence[iterator], len(freq_array) - 1)
        loop_over_elements(iterator + 1, end)

    loop_over_elements(0, len(input_sequence) - 1)

    result_value = -1
    for candidate_value in range(1, len(freq_array)):
        if freq_array[candidate_value] >= candidate_value:
            result_value = candidate_value

    return result_value