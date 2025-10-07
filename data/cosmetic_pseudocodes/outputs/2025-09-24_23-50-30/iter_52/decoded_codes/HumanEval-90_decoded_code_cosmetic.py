from typing import List, Optional, TypeVar

T = TypeVar('T')

def next_smallest(container: List[T]) -> Optional[T]:
    def build_sorted(distinct_items: List[T], accumulator: List[T]) -> List[T]:
        if not distinct_items:
            return accumulator
        head_element = distinct_items[0]
        tail_segment = distinct_items[1:]
        if head_element in accumulator:
            return build_sorted(tail_segment, accumulator)
        extended_accumulator = accumulator + [head_element]
        return build_sorted(tail_segment, extended_accumulator)

    def insertion_sort(collection: List[T]) -> List[T]:
        if not collection:
            return []
        first_part = collection[0]
        remaining_part = collection[1:]

        def insert_element(sorted_sublist: List[T], element: T) -> List[T]:
            if not sorted_sublist:
                return [element]
            first_sorted = sorted_sublist[0]
            rest_sorted = sorted_sublist[1:]
            if element <= first_sorted:
                return [element] + sorted_sublist
            return [first_sorted] + insert_element(rest_sorted, element)

        sorted_remaining = insertion_sort(remaining_part)
        return insert_element(sorted_remaining, first_part)

    removed_duplicates = build_sorted(container, [])
    sorted_unique_collection = insertion_sort(removed_duplicates)

    if len(sorted_unique_collection) < 2:
        return None
    return sorted_unique_collection[1]