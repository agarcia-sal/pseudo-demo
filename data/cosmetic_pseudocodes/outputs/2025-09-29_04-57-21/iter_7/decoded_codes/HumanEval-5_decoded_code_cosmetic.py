from typing import Sequence, TypeVar, List

T = TypeVar('T')
S = TypeVar('S')

def intersperse(input_sequence: Sequence[T], sep: S) -> List[T | S]:
    if not input_sequence:
        return []
    assembled: List[T | S] = []
    idx = 0
    while idx < len(input_sequence) - 1:
        assembled.append(input_sequence[idx])
        assembled.append(sep)
        idx += 1
    assembled.append(input_sequence[-1])
    return assembled