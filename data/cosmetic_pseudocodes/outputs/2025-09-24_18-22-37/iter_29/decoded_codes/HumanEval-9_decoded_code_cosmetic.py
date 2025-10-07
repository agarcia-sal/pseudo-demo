from typing import Sequence, List, Optional, TypeVar

T = TypeVar('T')

def rolling_max(sequence_input: Sequence[T]) -> List[T]:
    accumulator: Optional[T] = None
    output_sequence: List[T] = []

    iterator_idx = 0
    while iterator_idx < len(sequence_input):
        current_element = sequence_input[iterator_idx]
        if accumulator is None:
            accumulator = current_element
        else:
            candidate_max = accumulator
            alt_value = current_element
            if candidate_max >= alt_value:
                accumulator = candidate_max
            else:
                accumulator = alt_value
        output_sequence.append(accumulator)
        iterator_idx += 1

    return output_sequence