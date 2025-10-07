from typing import List, Optional, Sequence

def rolling_max(array_of_values: Sequence[float]) -> List[float]:
    accumulator: Optional[float] = None
    output_sequence: List[float] = []

    iterator_position: int = 0
    length = len(array_of_values)
    while iterator_position < length:
        current_element = array_of_values[iterator_position]
        if accumulator is None:
            accumulator = current_element
        else:
            if accumulator < current_element:
                accumulator = current_element
        output_sequence.append(accumulator)
        iterator_position += 1

    return output_sequence