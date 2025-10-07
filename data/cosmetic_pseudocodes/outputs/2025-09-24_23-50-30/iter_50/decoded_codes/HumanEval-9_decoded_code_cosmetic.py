from typing import List, Optional

def rolling_max(list_of_numbers: List[float]) -> List[float]:
    accumulator_result: List[float] = []
    current_peak: Optional[float] = None
    index: int = 0
    length: int = len(list_of_numbers)

    while index < length:
        element: float = list_of_numbers[index]
        if current_peak is None:
            current_peak = element
        else:
            # Update current_peak if element is greater than current_peak
            if element > current_peak:
                current_peak = element
        accumulator_result.append(current_peak)
        index += 1

    return accumulator_result