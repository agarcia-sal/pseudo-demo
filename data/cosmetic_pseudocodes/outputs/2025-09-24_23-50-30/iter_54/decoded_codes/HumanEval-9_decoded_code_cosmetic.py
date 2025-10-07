from typing import List, Optional


def rolling_max(sequence_of_values: List[int]) -> List[int]:
    current_peak: Optional[int] = None
    accumulated_maxes: List[int] = []

    def process_index(i: int) -> None:
        nonlocal current_peak
        if i < len(sequence_of_values):
            element = sequence_of_values[i]
            if current_peak is None:
                current_peak = element
            else:
                if current_peak < element:
                    current_peak = element
            accumulated_maxes.append(current_peak)
            process_index(i + 1)

    process_index(0)
    return accumulated_maxes