from typing import Sequence, TypeVar

T = TypeVar('T', bound='Comparable')

# Define Comparable protocol for type hinting sequences of comparable elements
class Comparable:
    def __lt__(self, other: 'Comparable') -> bool: ...
    def __gt__(self, other: 'Comparable') -> bool: ...

def monotonic(sequence: Sequence[T]) -> bool:
    sorted_inc = sorted(sequence)
    sorted_dec = sorted(sequence, reverse=True)
    if list(sequence) == sorted_inc:
        return True
    elif list(sequence) == sorted_dec:
        return True
    else:
        return False