from typing import Sequence, TypeVar

T = TypeVar('T')

def monotonic(sequence: Sequence[T]) -> bool:
    is_sorted_asc: bool = True
    is_sorted_desc: bool = True
    index: int = 0
    length: int = len(sequence)
    while True:
        if index >= length - 1:
            break
        current = sequence[index]
        next_element = sequence[index + 1]
        if current > next_element:
            is_sorted_asc = False
        if current < next_element:
            is_sorted_desc = False
        if not is_sorted_asc and not is_sorted_desc:
            break
        index += 1
    if is_sorted_asc or is_sorted_desc:
        return True
    return False