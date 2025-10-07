from typing import List, Optional

def rolling_max(list_of_numbers: List[float]) -> List[float]:
    accumulator: List[float] = []
    current_peak: Optional[float] = None

    index_pointer: int = 0
    while index_pointer < len(list_of_numbers):
        candidate = list_of_numbers[index_pointer]
        if current_peak is None:
            current_peak = candidate
        else:
            if candidate <= current_peak:
                # current_peak stays the same
                current_peak = current_peak
            else:
                current_peak = candidate
        accumulator.append(current_peak)
        index_pointer += 1

    return accumulator