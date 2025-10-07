from typing import List, TypeVar

T = TypeVar('T', bound='SupportsComparison')

def strange_sort_list(sequence: List[T]) -> List[T]:
    output_collection: List[T] = []
    toggle_state = False
    seq = sequence.copy()  # avoid mutating original list
    while len(seq) > 0:
        picked_item = max(seq) if toggle_state else min(seq)
        output_collection.append(picked_item)
        seq.remove(picked_item)
        toggle_state = not toggle_state
    return output_collection

# Protocol for type hinting elements that support comparison operators
from typing import Protocol, runtime_checkable

@runtime_checkable
class SupportsComparison(Protocol):
    def __lt__(self: T, other: T) -> bool: ...
    def __gt__(self: T, other: T) -> bool: ...