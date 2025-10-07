from typing import Sequence, TypeVar, List

T = TypeVar('T')

def intersperse(input_sequence: Sequence[T], separator: T) -> List[T]:
    if not input_sequence:
        return []

    aggregated_result: List[T] = []
    position = 0
    while position < len(input_sequence) - 1:
        aggregated_result.append(input_sequence[position])
        aggregated_result.append(separator)
        position += 1
    aggregated_result.append(input_sequence[-1])

    return aggregated_result