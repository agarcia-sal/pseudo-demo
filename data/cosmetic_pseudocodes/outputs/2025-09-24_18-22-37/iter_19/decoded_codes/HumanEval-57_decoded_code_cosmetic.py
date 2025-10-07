from typing import Sequence, TypeVar

T = TypeVar('T')


def monotonic(sequence: Sequence[T]) -> bool:
    flag1: bool = True  # Non-increasing flag
    flag2: bool = True  # Non-decreasing flag
    len_seq: int = len(sequence)
    index: int = 1
    while index <= len_seq - 1 and (flag1 or flag2):
        if sequence[index - 1] > sequence[index]:
            flag1 = False
        if sequence[index - 1] < sequence[index]:
            flag2 = False
        index += 1
    return flag1 or flag2