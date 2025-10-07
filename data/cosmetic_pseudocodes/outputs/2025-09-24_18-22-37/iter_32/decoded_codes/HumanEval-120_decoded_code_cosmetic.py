from typing import List


def maximum(list_of_numbers: List[int], count: int) -> List[int]:
    if count == 0:
        return []
    sorted_numbers = sorted(list_of_numbers)
    total_length = len(sorted_numbers)
    start_index = total_length - count
    result: List[int] = []
    current_pos = start_index
    while current_pos < total_length:
        result.append(sorted_numbers[current_pos])
        current_pos += 1
    return result