from typing import List

def get_positive(list_of_numbers: List[int]) -> List[int]:
    filtered_numbers: List[int] = []
    idx: int = 0

    while idx < len(list_of_numbers):
        current_number: int = list_of_numbers[idx]

        if current_number <= 0:
            idx += 1
            continue

        filtered_numbers.append(current_number)
        idx += 1

    return filtered_numbers