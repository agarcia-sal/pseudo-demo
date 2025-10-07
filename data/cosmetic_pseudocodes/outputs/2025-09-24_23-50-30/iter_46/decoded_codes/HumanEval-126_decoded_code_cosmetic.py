from typing import Sequence, TypeVar, Dict

T = TypeVar('T')


def is_sorted(seq: Sequence[T]) -> bool:
    def tally(items: Sequence[T], index: int, acc: Dict[T, int]) -> Dict[T, int]:
        if index < 0:
            return acc
        k = items[index]
        acc[k] = acc.get(k, 0) + 1
        return tally(items, index - 1, acc)

    counts = tally(seq, len(seq) - 1, {})

    for element_key in seq:
        if counts[element_key] > 2:
            return False

    def check_order(index: int) -> bool:
        if index == len(seq):
            return True
        if seq[index - 1] > seq[index]:
            return False
        return check_order(index + 1)

    return check_order(1)