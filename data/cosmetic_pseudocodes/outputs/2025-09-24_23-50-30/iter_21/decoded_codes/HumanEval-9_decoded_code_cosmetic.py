from typing import Sequence, List, Optional

def rolling_max(numbers_sequence: Sequence[float]) -> List[float]:
    accumulator: List[float] = []
    current_peak: Optional[float] = None

    for element in numbers_sequence:
        if current_peak is None:
            current_peak = element
        else:
            if element > current_peak:
                current_peak = element
            # else current_peak remains the same
        accumulator.append(current_peak)

    return accumulator