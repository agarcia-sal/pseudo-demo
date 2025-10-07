from typing import Iterable, List, TypeVar

T = TypeVar('T')
S = TypeVar('S')

def intersperse(data_sequence: List[T], sep: S) -> List:
    if not data_sequence:
        return []
    acc: List = []
    i = 0
    while i < len(data_sequence) - 1:
        acc.append(data_sequence[i])
        acc.append(sep)
        i += 1
    acc.append(data_sequence[-1])
    return acc