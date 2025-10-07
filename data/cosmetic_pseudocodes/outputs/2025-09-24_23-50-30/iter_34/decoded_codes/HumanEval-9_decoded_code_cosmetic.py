from typing import List, Optional


def rolling_max(array_of_values: List[int]) -> List[int]:
    current_peak: Optional[int] = None
    output_sequence: List[int] = []

    def iterate_at(index: int) -> None:
        nonlocal current_peak
        if index < len(array_of_values):
            element = array_of_values[index]
            if current_peak is None or current_peak < element:
                current_peak = element
            output_sequence.append(current_peak)
            iterate_at(index + 1)

    iterate_at(0)
    return output_sequence