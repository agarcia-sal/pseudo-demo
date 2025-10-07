from collections import Counter
from typing import Sequence, List, TypeVar

T = TypeVar('T')

def remove_duplicates(puzzle: Sequence[T]) -> List[T]:
    tally: Counter[T] = Counter(puzzle)
    result: List[T] = []
    cursor: int = 0
    while cursor < len(puzzle):
        element = puzzle[cursor]
        if tally[element] <= 1:
            result.append(element)
        cursor += 1
    return result