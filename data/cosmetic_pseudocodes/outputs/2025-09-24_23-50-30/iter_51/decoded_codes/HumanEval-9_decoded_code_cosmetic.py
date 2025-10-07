from typing import List, Optional

def rolling_max(sequence: List[int]) -> List[int]:
    def accumulate_max(index: int, current_peak: Optional[int], accumulator: List[int]) -> List[int]:
        if index == len(sequence):
            return accumulator
        candidate = sequence[index]
        updated_peak = candidate if current_peak is None else (candidate if candidate >= current_peak else current_peak)
        return accumulate_max(index + 1, updated_peak, accumulator + [updated_peak])
    return accumulate_max(0, None, [])