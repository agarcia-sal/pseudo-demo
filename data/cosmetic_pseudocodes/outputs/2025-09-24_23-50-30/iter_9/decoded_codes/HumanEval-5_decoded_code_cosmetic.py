from typing import TypeVar, Sequence, List

T = TypeVar('T')

def intersperse(sequence: Sequence[T], sep: T) -> List[T]:
    if not sequence:
        return []
    output: List[T] = []
    idx = 0
    while idx < len(sequence) - 1:
        output.append(sequence[idx])
        output.append(sep)
        idx += 1
    output.append(sequence[-1])
    return output