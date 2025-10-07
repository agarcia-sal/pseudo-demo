from typing import TypeVar, Sequence, List

T = TypeVar('T')

def intersperse(data_sequence: Sequence[T], glue: T) -> List[T]:
    def recursive_helper(index: int, acc: List[T]) -> List[T]:
        if index >= len(data_sequence):
            return acc
        if index == len(data_sequence) - 1:
            return acc + [data_sequence[index]]
        return recursive_helper(index + 1, acc + [data_sequence[index], glue])

    if not data_sequence:
        return []
    return recursive_helper(0, [])