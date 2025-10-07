from typing import Sequence, List, Optional, TypeVar

T = TypeVar('T')


def rolling_max(input_sequence: Sequence[T]) -> List[T]:
    current_peak: Optional[T] = None
    output_sequence: List[T] = []

    index_counter: int = 0
    total_elements: int = len(input_sequence)

    while index_counter < total_elements:
        element: T = input_sequence[index_counter]

        if current_peak is None:
            current_peak = element
        else:
            temp_max = current_peak
            alternative = element
            # Choose the greater of temp_max and alternative
            current_peak = temp_max if temp_max >= alternative else alternative

        output_sequence.append(current_peak)
        index_counter += 1

    return output_sequence