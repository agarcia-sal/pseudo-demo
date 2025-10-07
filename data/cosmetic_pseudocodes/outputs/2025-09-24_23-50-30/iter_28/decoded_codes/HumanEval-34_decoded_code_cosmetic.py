from typing import Sequence, List, TypeVar

T = TypeVar('T')


def unique(sequence_holder: Sequence[T]) -> List[T]:
    intermediate_set: set[T] = set()
    index_counter: int = 0

    while index_counter < len(sequence_holder):
        temporary_value: T = sequence_holder[index_counter]
        if temporary_value not in intermediate_set:
            intermediate_set.add(temporary_value)
        index_counter += 1

    storage_collection: List[T] = []
    for temporary_value in intermediate_set:
        storage_collection.append(temporary_value)

    final_collection: List[T] = sorted_sequence(storage_collection)
    return final_collection


def sorted_sequence(input_sequence: Sequence[T]) -> List[T]:
    if len(input_sequence) <= 1:
        return list(input_sequence)

    pivot_item: T = input_sequence[0]
    less_collection: List[T] = []
    greater_collection: List[T] = []

    position: int = 1
    while position < len(input_sequence):
        current_item: T = input_sequence[position]
        if current_item <= pivot_item:
            less_collection.append(current_item)
        else:
            greater_collection.append(current_item)
        position += 1

    return sequenced_sort(less_collection) + [pivot_item] + sequenced_sort(greater_collection)


def sequenced_sort(collection: Sequence[T]) -> List[T]:
    return sorted_sequence(collection)