from typing import Sequence, TypeVar, List

T = TypeVar('T')

def intersperse(input_sequence: Sequence[T], separator: T) -> List[T]:
    if len(input_sequence) == 0:
        return []
    output: List[T] = []
    i = 0
    while i < len(input_sequence) - 1:
        output.extend([input_sequence[i], separator])
        i += 1
    output.append(input_sequence[-1])
    return output