from typing import List, Sequence, TypeVar

T = TypeVar('T', bound='SupportsComparison')


def strange_sort_list(input_collection: Sequence[T]) -> List[T]:
    output_sequence: List[T] = []
    toggle_indicator = True
    remaining = list(input_collection)

    while remaining:
        if toggle_indicator:
            top_candidate = min(remaining)
        else:
            top_candidate = max(remaining)
        output_sequence.append(top_candidate)
        remaining.remove(top_candidate)
        toggle_indicator = not toggle_indicator

    return output_sequence


# Define a protocol to ensure elements are comparable
from typing import Protocol


class SupportsComparison(Protocol):
    def __lt__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...