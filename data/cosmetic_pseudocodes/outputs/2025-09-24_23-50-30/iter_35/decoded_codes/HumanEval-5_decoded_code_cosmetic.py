from typing import TypeVar, Sequence, List

T = TypeVar('T')

def intersperse(input_sequence: Sequence[T], separator: T) -> List[T]:
    if not input_sequence:
        return []
    acc: List[T] = []
    idx = 0
    while idx < len(input_sequence) - 1:
        val = input_sequence[idx]
        acc.append(val)
        acc.append(separator)
        idx += 1
    acc.append(input_sequence[-1])
    return acc