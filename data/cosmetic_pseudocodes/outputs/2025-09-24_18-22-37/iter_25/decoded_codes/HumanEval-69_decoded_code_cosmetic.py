from typing import List

def search(array_of_numbers: List[int]) -> int:
    counts: List[int] = []
    maximum: int = 0

    for element in array_of_numbers:
        if element > maximum:
            maximum = element

    length_of_counts: int = maximum + 1
    counts = [0] * length_of_counts

    idx: int = 0
    while idx < len(array_of_numbers):
        num = array_of_numbers[idx]
        counts[num] += 1
        idx += 1

    result_value: int = -1
    position: int = 1
    while position < len(counts):
        count_at_pos = counts[position]
        if not (count_at_pos < position):
            result_value = position
        position += 1

    return result_value