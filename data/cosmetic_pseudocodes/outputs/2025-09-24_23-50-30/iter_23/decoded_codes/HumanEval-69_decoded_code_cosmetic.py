from typing import List

def search(collection_of_numbers: List[int]) -> int:
    max_value = max(collection_of_numbers, default=-1)
    counts: List[int] = [0] * (max_value + 1)

    def accumulate(position: int) -> None:
        if position >= len(collection_of_numbers):
            return
        current_element = collection_of_numbers[position]
        counts[current_element] += 1
        accumulate(position + 1)

    accumulate(1)

    result = -1
    cursor = 1
    while cursor < len(counts):
        if not (counts[cursor] < cursor):
            result = cursor
        cursor += 1

    return result