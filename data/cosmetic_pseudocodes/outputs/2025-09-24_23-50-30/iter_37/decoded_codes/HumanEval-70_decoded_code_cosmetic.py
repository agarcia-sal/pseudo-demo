from typing import List, TypeVar

T = TypeVar('T', bound='Comparable')

class Comparable:
    def __lt__(self: T, other: T) -> bool: ...
    def __gt__(self: T, other: T) -> bool: ...

def strange_sort_list(sequence_of_values: List[T]) -> List[T]:
    collection_result: List[T] = []
    toggle_indicator: bool = True
    values = sequence_of_values.copy()  # avoid mutating input
    while values:
        if toggle_indicator:
            candidate = min(values)
        else:
            candidate = max(values)
        collection_result.append(candidate)
        values.remove(candidate)
        toggle_indicator = not toggle_indicator
    return collection_result