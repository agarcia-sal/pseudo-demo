from typing import List, Optional

def rolling_max(list_of_numbers: List[int]) -> List[int]:
    highest_so_far: Optional[int] = None
    accumulator: List[int] = []

    iterator: int = 0
    while iterator < len(list_of_numbers):
        element: int = list_of_numbers[iterator]

        if highest_so_far is None:
            highest_so_far = element
        else:
            if element > highest_so_far:
                highest_so_far = element

        accumulator.append(highest_so_far)
        iterator += 1

    return accumulator