from typing import List, TypeVar, Sequence

T = TypeVar('T')
S = TypeVar('S')

def intersperse(array_input: Sequence[T], separator: S) -> List:
    if not array_input:
        return []
    output_sequence: List = []
    last_index = len(array_input) - 1
    current_index = 0
    while current_index < last_index:
        output_sequence.append(array_input[current_index])
        output_sequence.append(separator)
        current_index += 1
    output_sequence.append(array_input[last_index])
    return output_sequence