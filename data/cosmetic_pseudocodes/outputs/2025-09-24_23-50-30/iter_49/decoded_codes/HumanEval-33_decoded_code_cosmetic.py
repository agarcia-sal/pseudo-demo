from typing import List, Any


def sort_third(list_input: List[Any]) -> List[Any]:
    def reorder_at_triples(array_data: List[Any]) -> None:
        def group_by_step(offset: int, collection: List[Any], accumulator: List[Any]) -> List[Any]:
            if offset >= len(collection):
                return accumulator
            return group_by_step(offset + 3, collection, accumulator + [collection[offset]])

        def overwrite_by_indices(target: List[Any], replacements: List[Any], index: int, limit: int) -> None:
            if index >= limit:
                return
            target[index] = replacements[0]
            overwrite_by_indices(target, replacements[1:], index + 3, limit)

        triple_indexes_elements = group_by_step(0, array_data, [])
        sorted_triples = sorted(triple_indexes_elements)
        overwrite_by_indices(array_data, sorted_triples, 0, len(array_data))

    copied_sequence: List[Any] = []
    for element_index in range(len(list_input)):
        copied_sequence = copied_sequence + [list_input[element_index]]

    reorder_at_triples(copied_sequence)
    return copied_sequence