from typing import TypeVar, Sequence, List

T = TypeVar('T')

def intersperse(sequence: Sequence[T], sep: T) -> List[T]:
    if len(sequence) == 0:
        return []
    output: List[T] = []
    index = 0
    while index < len(sequence) - 1:
        output.append(sequence[index])
        output.append(sep)
        index += 1
    output.append(sequence[-1])
    return output