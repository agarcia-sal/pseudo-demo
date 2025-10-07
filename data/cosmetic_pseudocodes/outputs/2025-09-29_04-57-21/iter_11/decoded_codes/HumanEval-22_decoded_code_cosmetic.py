from typing import List, Any

def filter_integers(list_of_values: List[Any]) -> List[int]:
    output_collection: List[int] = []
    iterator_index: int = 0

    while iterator_index < len(list_of_values):
        current_item = list_of_values[iterator_index]

        if not isinstance(current_item, int):
            iterator_index += 1
            continue

        output_collection.append(current_item)
        iterator_index += 1

    return output_collection