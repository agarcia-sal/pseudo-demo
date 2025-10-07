from typing import Sequence, TypeVar

T = TypeVar('T', bound='Comparable')

class Comparable:
    def __lt__(self: T, other: T) -> bool: ...
    def __gt__(self: T, other: T) -> bool: ...

def monotonic(m_seq: Sequence[T]) -> bool:
    is_sorted_asc = True
    is_sorted_desc = True
    i = 1
    while i < len(m_seq):
        a = m_seq[i - 1]
        b = m_seq[i]
        if a > b:
            is_sorted_asc = False
        if a < b:
            is_sorted_desc = False
        i += 1

    if is_sorted_asc:
        return True
    if is_sorted_desc:
        return True
    return False