from typing import Iterable, List, TypeVar, Set

T = TypeVar('T')


def unique(collection_of_items: Iterable[T]) -> List[T]:
    def to_sorted_list(input_set: Set[T], accumulator: List[T]) -> List[T]:
        if not input_set:
            return accumulator
        min_element = min(input_set)
        return to_sorted_list(input_set - {min_element}, accumulator + [min_element])

    distinct_items: Set[T] = set()
    for element in collection_of_items:
        distinct_items.add(element)

    return to_sorted_list(distinct_items, [])