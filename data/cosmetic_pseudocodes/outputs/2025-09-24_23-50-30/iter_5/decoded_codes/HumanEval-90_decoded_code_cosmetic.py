from typing import Iterable, Optional, Set, TypeVar, List

T = TypeVar('T')

def next_smallest(sequence: Iterable[T]) -> Optional[T]:
    def helper(seq: Iterable[T], acc: Set[T]) -> Set[T]:
        seq_iter = iter(seq)
        try:
            current = next(seq_iter)
        except StopIteration:
            return acc
        acc.add(current)
        return helper(seq_iter, acc)

    distinct_items = helper(sequence, set())
    ordered_items: List[T] = sorted(distinct_items)
    if len(ordered_items) <= 1:
        return None
    return ordered_items[1]