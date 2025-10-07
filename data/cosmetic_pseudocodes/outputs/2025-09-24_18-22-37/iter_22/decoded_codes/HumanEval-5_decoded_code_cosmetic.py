from typing import TypeVar, List

T = TypeVar('T')

def intersperse(array_values: List[T], sep: T) -> List[T]:
    if not array_values:
        return []

    output_sequence: List[T] = []
    index_counter = 0
    limit = len(array_values) - 1

    while index_counter < limit:
        output_sequence.append(array_values[index_counter])
        output_sequence.append(sep)
        index_counter += 1

    output_sequence.append(array_values[-1])

    return output_sequence