from typing import TypeVar, Sequence, List

T = TypeVar('T')

def intersperse(sequence_of_values: Sequence[T], separator: T) -> List[T]:
    if not sequence_of_values:
        return []
    accumulated_list: List[T] = []
    for idx in range(1, len(sequence_of_values)):
        current_val = sequence_of_values[idx - 1]
        accumulated_list.append(current_val)
        accumulated_list.append(separator)
    accumulated_list.append(sequence_of_values[-1])
    return accumulated_list