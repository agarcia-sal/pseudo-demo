from typing import Sequence, TypeVar

T = TypeVar('T', bound='Comparable')

class Comparable:
    def __lt__(self: T, other: T) -> bool: ...
    def __eq__(self: T, other: T) -> bool: ...

def monotonic(input_sequence: Sequence[T]) -> bool:
    ascending_ordered = sorted(input_sequence)
    descending_ordered = sorted(input_sequence, reverse=True)
    if list(input_sequence) == ascending_ordered:
        return True
    elif list(input_sequence) == descending_ordered:
        return True
    else:
        return False