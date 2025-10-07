from typing import List

def solution(sequence_of_numbers: List[int]) -> int:
    def accumulate(candidate_collection: List[int], current_index: int) -> List[int]:
        if current_index >= len(sequence_of_numbers):
            return candidate_collection
        if (current_index % 2 == 0) and (sequence_of_numbers[current_index] % 2 == 1):
            accumulator = candidate_collection + [sequence_of_numbers[current_index]]
        else:
            accumulator = candidate_collection
        return accumulate(accumulator, current_index + 1)

    filtered_elements = accumulate([], 0)
    total_sum = sum(filtered_elements)
    return total_sum