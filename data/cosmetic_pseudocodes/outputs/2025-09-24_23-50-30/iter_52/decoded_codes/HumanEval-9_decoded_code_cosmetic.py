from typing import List, Optional, Sequence


def rolling_max(data_sequence: Sequence[int]) -> List[int]:
    def helper(index: int, current_peak: Optional[int], accumulator: List[int]) -> List[int]:
        if index == len(data_sequence):
            return accumulator

        element = data_sequence[index]
        updated_peak = element if current_peak is None or element > current_peak else current_peak

        accumulator.append(updated_peak)

        return helper(index + 1, updated_peak, accumulator)

    return helper(0, None, [])