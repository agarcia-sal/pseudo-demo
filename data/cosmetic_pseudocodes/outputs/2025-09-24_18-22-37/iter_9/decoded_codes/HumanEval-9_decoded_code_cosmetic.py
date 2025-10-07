from typing import Sequence, List, Optional, TypeVar, Union

T = TypeVar('T', bound=Union[int, float]]

def rolling_max(sequence_values: Sequence[T]) -> List[T]:
    result_listing: List[T] = []
    accumulator: Optional[T] = None

    index: int = 0
    length: int = len(sequence_values)
    while index < length:
        current_element: T = sequence_values[index]

        if accumulator is not None:
            temp_max = accumulator
            # Choose the greater of temp_max and current_element without direct max()
            accumulator = (temp_max if temp_max >= current_element else current_element)
        else:
            accumulator = current_element

        result_listing.append(accumulator)
        index += 1

    return result_listing