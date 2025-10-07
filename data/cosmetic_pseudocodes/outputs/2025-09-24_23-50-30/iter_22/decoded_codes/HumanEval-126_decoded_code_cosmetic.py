from typing import Sequence, TypeVar, Dict, List

T = TypeVar('T')

def is_sorted(collection: Sequence[T]) -> bool:
    tally: Dict[T, int] = {}

    def tally_elements(sequence: Sequence[T], index: int) -> None:
        if index == len(sequence):
            return
        key = sequence[index]
        tally[key] = tally.get(key, 0) + 1
        tally_elements(sequence, index + 1)

    tally_elements(collection, 0)

    def has_excess_duplicates(keys: List[T]) -> bool:
        if not keys:
            return False
        head, tail = keys[0], keys[1:]
        if tally[head] > 2:
            return True
        return has_excess_duplicates(tail)

    if has_excess_duplicates(list(collection)):
        return False

    def check_non_decreasing(sequence: Sequence[T], pointer: int) -> bool:
        if pointer == len(sequence):
            return True
        if sequence[pointer - 1] > sequence[pointer]:
            return False
        return check_non_decreasing(sequence, pointer + 1)

    return check_non_decreasing(collection, 1)