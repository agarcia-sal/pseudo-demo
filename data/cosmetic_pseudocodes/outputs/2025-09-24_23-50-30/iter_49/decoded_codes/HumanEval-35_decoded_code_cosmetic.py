from typing import Sequence, TypeVar

T = TypeVar('T')

def max_element(collection_items: Sequence[T]) -> T:
    if not collection_items:
        raise ValueError("max_element() arg is an empty sequence")

    def find_maximum(index_cursor: int, current_peak: T) -> T:
        if index_cursor >= len(collection_items):
            return current_peak
        inspected = collection_items[index_cursor]
        candidate_candidate = inspected if inspected > current_peak else current_peak
        return find_maximum(index_cursor + 1, candidate_candidate)

    return find_maximum(1, collection_items[0])