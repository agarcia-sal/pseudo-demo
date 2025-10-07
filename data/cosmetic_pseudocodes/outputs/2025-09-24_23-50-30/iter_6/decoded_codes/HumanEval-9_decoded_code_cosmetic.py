from typing import List, Optional

def rolling_max(list_of_numbers: List[float]) -> List[float]:
    accumulator: List[float] = []
    index: int = 0
    current_largest: Optional[float] = None

    while index < len(list_of_numbers):
        candidate = list_of_numbers[index]

        if current_largest is None:
            current_largest = candidate
        else:
            current_largest = (current_largest + candidate + abs(current_largest - candidate)) / 2

        accumulator.append(current_largest)
        index += 1

    return accumulator