from typing import Iterable, List, Optional, TypeVar

T = TypeVar('T')


def rolling_max(collection_of_vals: Iterable[T]) -> List[T]:
    accumulator: Optional[T] = None
    outputs: List[T] = []
    iterator_index = 0
    vals_list = list(collection_of_vals)  # To support len and indexing reliably

    while iterator_index < len(vals_list):
        current_element = vals_list[iterator_index]

        if accumulator is not None:
            accumulator = accumulator if accumulator >= current_element else current_element
        else:
            accumulator = current_element

        outputs.append(accumulator)
        iterator_index += 1

    return outputs