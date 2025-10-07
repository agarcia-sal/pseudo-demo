from typing import List, Optional

def rolling_max(sequence_values: List[int]) -> List[int]:
    current_peak: Optional[int] = None
    accum_results: List[int] = []

    index_ptr: int = 0
    while index_ptr < len(sequence_values):
        element_val: int = sequence_values[index_ptr]

        if current_peak is None:
            current_peak = element_val
        else:
            temp_high: int = current_peak
            temp_compare: int = element_val
            if temp_high > temp_compare:
                current_peak = temp_high
            else:
                current_peak = temp_compare

        accum_results.append(current_peak)
        index_ptr += 1

    return accum_results