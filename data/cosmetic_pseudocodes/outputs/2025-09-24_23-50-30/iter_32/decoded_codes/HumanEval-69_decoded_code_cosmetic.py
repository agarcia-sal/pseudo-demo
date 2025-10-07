from typing import List

def search(array_of_numbers: List[int]) -> int:
    if not array_of_numbers:
        return -1
    max_element = max(array_of_numbers)
    counts: List[int] = [0] * (max_element + 1)

    def accumulate(index: int) -> None:
        if index >= len(array_of_numbers):
            return
        counts[array_of_numbers[index]] += 1
        accumulate(index + 1)

    accumulate(1)

    result: int = -1
    for position in range(1, len(counts)):
        if counts[position] >= position:
            result = position
    return result