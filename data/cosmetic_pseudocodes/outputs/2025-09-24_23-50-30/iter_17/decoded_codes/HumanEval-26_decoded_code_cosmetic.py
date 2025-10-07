from collections.abc import Sequence
from typing import TypeVar, List

T = TypeVar("T")

def remove_duplicates(sequence: Sequence[T]) -> List[T]:
    occurrence_map: dict[T, int] = {}
    for item in sequence:
        occurrence_map[item] = occurrence_map.get(item, 0) + 1
    return [sequence[i] for i in range(len(sequence)) if occurrence_map[sequence[i]] <= 1]