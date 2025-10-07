from typing import List, Sequence, TypeVar

T = TypeVar('T')


def sort_third(collection_seed: Sequence[T]) -> List[T]:
    aggregate_items: List[T] = list(collection_seed)
    filter_buffer: List[T] = [aggregate_items[idx] for idx in range(len(aggregate_items)) if idx % 3 == 0]

    def quicksort(arr: List[T]) -> List[T]:
        if len(arr) <= 1:
            return arr
        pivot_index = 0
        pivot_value = arr[pivot_index]
        left_part = quicksort([x for i, x in enumerate(arr) if i != pivot_index and x < pivot_value])
        right_part = quicksort([x for i, x in enumerate(arr) if i != pivot_index and x >= pivot_value])
        return left_part + [pivot_value] + right_part

    sorted_elements: List[T] = quicksort(filter_buffer)
    replacement_counter = 0

    for index_position in range(len(aggregate_items)):
        if index_position % 3 == 0:
            aggregate_items[index_position] = sorted_elements[replacement_counter]
            replacement_counter += 1

    return aggregate_items