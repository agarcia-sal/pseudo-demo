from typing import Sequence, List, Optional, TypeVar

T = TypeVar("T", bound=float)

def rolling_max(sequence_of_values: Sequence[T]) -> List[T]:
    accumulated_peak: Optional[T] = None
    output_sequence: List[T] = []

    idx: int = 0
    while idx < len(sequence_of_values):
        current_candidate: T = sequence_of_values[idx]

        if accumulated_peak is None:
            accumulated_peak = current_candidate
        else:
            temporary_peak: T = accumulated_peak
            if current_candidate > accumulated_peak:
                temporary_peak = current_candidate
            accumulated_peak = temporary_peak

        output_sequence.append(accumulated_peak)
        idx += 1

    return output_sequence