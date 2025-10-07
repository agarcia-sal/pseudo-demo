from typing import Sequence, TypeVar

T = TypeVar('T')

def monotonic(sequence_of_items: Sequence[T]) -> bool:
    flag_forward: bool = True
    flag_backward: bool = True
    idx: int = 0

    while idx < len(sequence_of_items):
        if idx > 0:
            if sequence_of_items[idx] < sequence_of_items[idx - 1]:
                flag_forward = False
            if sequence_of_items[idx] > sequence_of_items[idx - 1]:
                flag_backward = False
        idx += 1

    if flag_forward:
        return True
    if flag_backward:
        return True

    return False