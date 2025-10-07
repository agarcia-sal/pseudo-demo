from typing import TypeVar, Sequence, List

T = TypeVar('T')

def intersperse(values_array: Sequence[T], separator: T) -> List[T]:
    if not values_array:
        return []
    output_sequence: List[T] = []
    idx = 0
    while idx < len(values_array) - 1:
        output_sequence.append(values_array[idx])
        output_sequence.append(separator)
        idx += 1
    output_sequence.append(values_array[-1])
    return output_sequence