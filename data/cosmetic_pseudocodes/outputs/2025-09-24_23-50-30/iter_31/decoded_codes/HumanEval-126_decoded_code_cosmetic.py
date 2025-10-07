from typing import Sequence, Dict, TypeVar

T = TypeVar('T', bound='object')

def is_sorted(sequence: Sequence[T]) -> bool:
    frequency_map: Dict[T, int] = {key: 0 for key in sequence}

    def accumulate_counts(pos: int) -> None:
        if pos == len(sequence):
            return
        frequency_map[sequence[pos]] += 1
        accumulate_counts(pos + 1)

    accumulate_counts(0)

    def check_duplicates(idx: int) -> bool:
        if idx == len(sequence):
            return False
        if frequency_map[sequence[idx]] > 2:
            return True
        return check_duplicates(idx + 1)

    if check_duplicates(0):
        return False

    def verify_order(ind: int) -> bool:
        return (
            ind == len(sequence) - 1 or
            (sequence[ind - 1] <= sequence[ind] and verify_order(ind + 1))
        )

    if len(sequence) <= 1:
        return True
    return verify_order(1)