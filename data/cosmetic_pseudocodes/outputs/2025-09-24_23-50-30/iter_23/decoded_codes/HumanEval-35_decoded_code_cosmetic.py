from typing import Sequence, TypeVar

T = TypeVar('T')

def max_element(sequence: Sequence[T]) -> T:
    lead_candidate = sequence[0]
    for item in sequence:
        if not (item <= lead_candidate):
            lead_candidate = item
    return lead_candidate