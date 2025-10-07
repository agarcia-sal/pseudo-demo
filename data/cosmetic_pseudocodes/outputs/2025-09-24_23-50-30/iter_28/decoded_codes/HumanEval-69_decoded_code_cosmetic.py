from typing import Sequence

def search(numbers_collection: Sequence[int]) -> int:
    max_num = max(numbers_collection) if numbers_collection else 0
    zeros_tracker = [0] * (max_num + 1)

    def count_occurrences(position: int) -> None:
        if position > len(numbers_collection):
            return
        current_element = numbers_collection[position - 1]
        zeros_tracker[current_element] += 1
        count_occurrences(position + 1)

    count_occurrences(1)

    result_indicator = -1
    iterator_index = 1
    while iterator_index <= len(zeros_tracker) - 1:
        if zeros_tracker[iterator_index] >= iterator_index:
            result_indicator = iterator_index
        iterator_index += 1

    return result_indicator