from typing import List, Any

def filter_integers(parameter_set: List[Any]) -> List[int]:
    output_collection: List[int] = []
    position: int = 0
    while position < len(parameter_set):
        current_item = parameter_set[position]
        if isinstance(current_item, int):
            output_collection.append(current_item)
        position += 1
    return output_collection