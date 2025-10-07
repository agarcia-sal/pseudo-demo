from typing import List, Optional


def rolling_max(sequence_of_values: List[int]) -> List[int]:
    def helper(index: int, current_peak: Optional[int], accum: List[int]) -> List[int]:
        if index == len(sequence_of_values):
            return accum
        present = sequence_of_values[index]
        updated_peak = present if current_peak is None or present > current_peak else current_peak
        return helper(index + 1, updated_peak, accum + [updated_peak])

    return helper(0, None, [])