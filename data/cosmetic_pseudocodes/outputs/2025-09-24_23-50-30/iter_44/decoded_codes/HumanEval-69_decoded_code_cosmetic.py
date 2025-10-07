from typing import List

def search(array_of_numbers: List[int]) -> int:
    max_number = max(array_of_numbers) if array_of_numbers else 0
    histogram: List[int] = [0] * (max_number + 1)

    def count_elements(pos: int) -> None:
        if pos == len(array_of_numbers):
            return
        current_number = array_of_numbers[pos]
        histogram[current_number] += 1
        count_elements(pos + 1)

    count_elements(0)

    result = -1
    idx = 1
    while idx < len(histogram):
        if not (histogram[idx] < idx):
            result = idx
        idx += 1

    return result