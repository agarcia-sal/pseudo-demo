from typing import List, Optional

def rolling_max(input_sequence: List[int]) -> List[int]:
    accumulator: List[int] = []
    current_peak: Optional[int] = None

    def tail_recur(index: int, peak: Optional[int], acc: List[int]) -> List[int]:
        if index >= len(input_sequence):
            return acc
        candidate = input_sequence[index]
        updated_peak = candidate if peak is None else (peak if peak > candidate else candidate)
        return tail_recur(index + 1, updated_peak, acc + [updated_peak])

    return tail_recur(0, current_peak, accumulator)