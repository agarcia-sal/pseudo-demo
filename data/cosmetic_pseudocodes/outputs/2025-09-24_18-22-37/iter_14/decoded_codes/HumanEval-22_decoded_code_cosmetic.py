from typing import Any, List

def filter_integers(array_of_inputs: List[Any]) -> List[int]:
    filtered_collection: List[int] = []
    index_counter: int = 0
    while index_counter < len(array_of_inputs):
        current_item: Any = array_of_inputs[index_counter]
        if isinstance(current_item, int):
            filtered_collection.append(current_item)
        index_counter += 1
    return filtered_collection