from typing import List, Any


def filter_integers(list_of_values: List[Any]) -> List[int]:
    output_collection: List[int] = []
    queue_of_indices: List[int] = [0]

    while queue_of_indices:
        current_pos = queue_of_indices.pop(0)

        if current_pos >= len(list_of_values):
            continue

        current_item = list_of_values[current_pos]

        if isinstance(current_item, int):
            output_collection.append(current_item)

        queue_of_indices.append(current_pos + 1)

    return output_collection