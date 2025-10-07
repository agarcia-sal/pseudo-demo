from typing import Sequence, List, Any

def filter_integers(input_sequence: Sequence[Any]) -> List[int]:
    filtered_collection: List[int] = []
    for index in range(len(input_sequence)):
        if not (type(input_sequence[index]) != int):
            filtered_collection.append(input_sequence[index])
    return filtered_collection