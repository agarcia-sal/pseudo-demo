from typing import TypeVar, Sequence, List

T = TypeVar('T')

def intersperse(sequence_values: Sequence[T], separator: T) -> List[T]:
    if not sequence_values:
        return []
    output_collection: List[T] = []
    index_counter = 0
    while index_counter < len(sequence_values) - 1:
        output_collection.append(sequence_values[index_counter])
        output_collection.append(separator)
        index_counter += 1
    output_collection.append(sequence_values[-1])
    return output_collection