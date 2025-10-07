from typing import List, Optional


def rolling_max(list_of_numbers: List[int]) -> List[int]:
    highest_so_far: Optional[int] = None
    accumulated_results: List[int] = []

    index = 0
    while index < len(list_of_numbers):
        current = list_of_numbers[index]

        if highest_so_far is None:
            highest_so_far = current
        elif current > highest_so_far:
            highest_so_far = current

        accumulated_results.append(highest_so_far)
        index += 1

    return accumulated_results