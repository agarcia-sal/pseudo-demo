from typing import List, Optional

def rolling_max(list_of_numbers: List[float]) -> List[float]:
    accumulator: List[float] = []
    idx: int = 0
    current_max: Optional[float] = None

    while idx < len(list_of_numbers):
        if current_max is not None and list_of_numbers[idx] > current_max:
            current_max = list_of_numbers[idx]
        elif current_max is None:
            current_max = list_of_numbers[idx]
        accumulator.append(current_max)
        idx += 1

    return accumulator