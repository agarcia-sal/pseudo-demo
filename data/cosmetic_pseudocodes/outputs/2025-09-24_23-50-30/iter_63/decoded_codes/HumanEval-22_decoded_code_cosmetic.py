from typing import Sequence, List, Any

def filter_integers(source_sequence: Sequence[Any]) -> List[int]:
    result_collection: List[int] = []
    for index in range(len(source_sequence)):
        current_item = source_sequence[index]
        if isinstance(current_item, int):
            result_collection.append(current_item)
    return result_collection