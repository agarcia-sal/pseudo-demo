from typing import Sequence, TypeVar

T = TypeVar('T')

def monotonic(seq_1: Sequence[T]) -> bool:
    proc_2 = sorted(seq_1)
    proc_3 = sorted(seq_1, reverse=True)
    return seq_1 == proc_2 or seq_1 == proc_3