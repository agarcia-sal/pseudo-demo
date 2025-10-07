from typing import Sequence, Optional, List, TypeVar

T = TypeVar("T")


def next_smallest(input_sequence: Sequence[T]) -> Optional[T]:
    def to_unique_ordered(collection: Sequence[T], result_accumulator: List[T]) -> List[T]:
        if not collection:
            return result_accumulator
        head_element, *tail_collection = collection
        if head_element in result_accumulator:
            return to_unique_ordered(tail_collection, result_accumulator)
        return to_unique_ordered(tail_collection, result_accumulator + [head_element])

    filtered_unique = to_unique_ordered(input_sequence, [])
    sorted_unique: List[T] = []
    while filtered_unique:
        smallest_element = filtered_unique[0]
        for each_element in filtered_unique:
            if each_element < smallest_element:
                smallest_element = each_element
        sorted_unique.append(smallest_element)
        filtered_unique = [x for x in filtered_unique if x != smallest_element]

    if len(sorted_unique) < 2:
        return None
    return sorted_unique[1]