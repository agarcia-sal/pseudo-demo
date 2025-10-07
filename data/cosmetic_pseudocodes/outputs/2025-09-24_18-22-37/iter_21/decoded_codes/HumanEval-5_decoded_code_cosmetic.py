from typing import TypeVar, Sequence, List

T = TypeVar('T')

def intersperse(sequence: Sequence[T], sep: T) -> List[T]:
    output: List[T] = []
    if sequence:
        idx = 0
        while idx < len(sequence) - 1:
            current = sequence[idx]
            output.append(current)
            output.append(sep)
            idx += 1
        output.append(sequence[len(sequence) - 1])
    return output