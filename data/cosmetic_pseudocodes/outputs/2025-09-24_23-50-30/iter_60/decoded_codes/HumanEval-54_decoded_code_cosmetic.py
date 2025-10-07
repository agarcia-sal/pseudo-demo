from typing import Sequence, Set, TypeVar

T = TypeVar('T', bound=str)

def same_chars(arg_a: Sequence[T], arg_b: Sequence[T]) -> bool:
    def fold_chars(seq: Sequence[T], acc: Set[T], idx: int) -> Set[T]:
        if idx == len(seq):
            return acc
        return fold_chars(seq, acc | {seq[idx]}, idx + 1)

    accumulated_1 = fold_chars(arg_a, set(), 0)
    accumulated_2 = fold_chars(arg_b, set(), 0)

    return accumulated_1 == accumulated_2