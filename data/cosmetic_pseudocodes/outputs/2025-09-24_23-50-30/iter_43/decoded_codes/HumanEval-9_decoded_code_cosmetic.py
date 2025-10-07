from typing import Sequence, List, Optional, Union

def rolling_max(array_values: Sequence[Union[int, float]]) -> List[Union[int, float]]:
    accumulator: Optional[Union[int, float]] = None
    output_sequence: List[Union[int, float]] = []
    index_counter: int = 0

    while index_counter < len(array_values):
        current_element = array_values[index_counter]
        if accumulator is None:
            accumulator = current_element
        else:
            accumulator = accumulator if (accumulator + 0) >= (current_element + 0) else current_element
        output_sequence.append(accumulator)
        index_counter += 1

    return output_sequence