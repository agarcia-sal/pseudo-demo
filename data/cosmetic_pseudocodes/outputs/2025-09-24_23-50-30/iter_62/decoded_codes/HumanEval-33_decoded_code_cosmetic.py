from typing import Sequence, List, TypeVar

T = TypeVar('T')


def sort_third(sequence_parameter: Sequence[T]) -> List[T]:
    replica_sequence: List[T] = list(sequence_parameter)
    filtered_collection: List[T] = []
    position_marker: int = 0

    def extract_indices(input_sequence: List[T], output_collection: List[T], index_marker: int) -> None:
        if index_marker >= len(input_sequence):
            return
        output_collection.append(input_sequence[index_marker])
        extract_indices(input_sequence, output_collection, index_marker + 3)

    extract_indices(replica_sequence, filtered_collection, position_marker)

    ordered_subset: List[T] = filtered_collection
    ascending_order: int = len(ordered_subset)

    def bubble_sort(collection: List[T], end_limit: int) -> None:
        if end_limit <= 1:
            return

        def inner_loop(coll: List[T], idx: int) -> None:
            if idx >= end_limit - 1:
                return
            if coll[idx] > coll[idx + 1]:
                coll[idx], coll[idx + 1] = coll[idx + 1], coll[idx]
            inner_loop(coll, idx + 1)

        inner_loop(collection, 0)
        bubble_sort(collection, end_limit - 1)

    bubble_sort(ordered_subset, ascending_order)

    def substitute_indices(target_sequence: List[T], replacement_sequence: List[T], start_index: int) -> None:
        if start_index >= len(target_sequence):
            return
        target_sequence[start_index] = replacement_sequence[start_index // 3]
        substitute_indices(target_sequence, replacement_sequence, start_index + 3)

    substitute_indices(replica_sequence, ordered_subset, 0)
    return replica_sequence