from typing import List, Any

def filter_integers(collection_parameter: List[Any]) -> List[int]:
    filtered_collection: List[int] = []
    idx: int = 0
    while idx < len(collection_parameter):
        current_item = collection_parameter[idx]
        if isinstance(current_item, int):
            filtered_collection.append(current_item)
        idx += 1
    return filtered_collection