from typing import Sequence, TypeVar

T = TypeVar('T')

def how_many_times(orig_seq: Sequence[T], seek_seq: Sequence[T]) -> int:
    tally: int = 0
    limit: int = len(orig_seq) - len(seek_seq)
    for cursor in range(limit + 1):
        if orig_seq[cursor : cursor + len(seek_seq)] == seek_seq:
            tally += 1
    return tally