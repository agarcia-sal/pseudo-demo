from typing import Sequence, TypeVar, List

T = TypeVar('T')

def intersperse(sequence: Sequence[T], sep: T) -> List[T]:
    if not sequence:
        return []

    output: List[T] = []
    index = 0

    while index < len(sequence) - 1:
        output.append(sequence[index])
        output.append(sep)
        index += 1

    output.append(sequence[-1])

    return output