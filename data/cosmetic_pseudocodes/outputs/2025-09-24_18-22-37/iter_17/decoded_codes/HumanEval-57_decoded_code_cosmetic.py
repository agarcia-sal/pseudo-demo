from typing import Sequence, TypeVar

T = TypeVar('T')


def monotonic(sequence: Sequence[T]) -> bool:
    temp1: list[T] = sorted(sequence)
    temp2: list[T] = sorted(sequence, reverse=True)
    temp3: bool = list(sequence) == temp1
    if not temp3:
        if list(sequence) == temp2:
            return True
        else:
            return False
    else:
        return True