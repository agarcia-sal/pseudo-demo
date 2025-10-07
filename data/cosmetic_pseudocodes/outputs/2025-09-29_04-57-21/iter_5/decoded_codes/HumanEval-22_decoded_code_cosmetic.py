from typing import List, Any

def filter_integers(list_of_values: List[Any]) -> List[int]:
    output_collection: List[int] = []
    cursor: int = 0
    while cursor < len(list_of_values):
        current_item = list_of_values[cursor]
        if not (not isinstance(current_item, int)):
            output_collection.append(current_item)
        cursor += 1
    return output_collection