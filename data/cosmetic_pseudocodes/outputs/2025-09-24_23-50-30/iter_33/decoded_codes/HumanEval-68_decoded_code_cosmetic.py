from typing import Sequence, List, Union


def pluck(sequence_of_items: Sequence[int]) -> List[Union[int, int]]:
    def find_minimum_and_index(
        collection: Sequence[int], idx_tracker: int, best_val: int, best_idx: int
    ) -> List[Union[int, int]]:
        if idx_tracker >= len(collection):
            return [best_val, best_idx]
        current_val = collection[idx_tracker]
        if current_val < best_val:
            return find_minimum_and_index(collection, idx_tracker + 1, current_val, idx_tracker)
        else:
            return find_minimum_and_index(collection, idx_tracker + 1, best_val, best_idx)

    if len(sequence_of_items) == 0:
        return []

    filtered_copy = [candidate for candidate in sequence_of_items if candidate % 2 == 0]

    if not filtered_copy:
        return []

    first_filtered_val = filtered_copy[0]
    first_filtered_idx = sequence_of_items.index(first_filtered_val)

    return find_minimum_and_index(sequence_of_items, 0, first_filtered_val, first_filtered_idx)