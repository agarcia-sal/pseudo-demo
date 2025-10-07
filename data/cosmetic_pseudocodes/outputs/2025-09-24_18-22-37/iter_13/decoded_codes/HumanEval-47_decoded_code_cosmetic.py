from typing import Sequence, TypeVar, Union

T = TypeVar('T', bound=Union[int, float])

def median(collection: Sequence[T]) -> float:
    ordered_collection = sorted(collection)
    size = len(ordered_collection)
    half_index = size // 2
    is_size_odd = (size % 2) == 1
    if not is_size_odd:
        left_value = ordered_collection[half_index - 1]
        right_value = ordered_collection[half_index]
        return (left_value + right_value) / 2.0
    return float(ordered_collection[half_index])