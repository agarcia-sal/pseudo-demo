from typing import Sequence, Optional, TypeVar

T = TypeVar('T')

def max_element(sequence_items: Sequence[T]) -> Optional[T]:
    if not sequence_items:
        return None

    def find_max(idx: int, curr_max: T) -> T:
        if idx == len(sequence_items):
            return curr_max
        next_candidate = sequence_items[idx]
        return find_max(idx + 1, curr_max if curr_max >= next_candidate else next_candidate)

    return find_max(1, sequence_items[0])