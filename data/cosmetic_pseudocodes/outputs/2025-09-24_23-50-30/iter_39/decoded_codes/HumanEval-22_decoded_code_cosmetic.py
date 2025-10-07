from typing import Sequence, List, Any

def filter_integers(sequence: Sequence[Any]) -> List[int]:
    filtered_result: List[int] = []
    index_counter: int = 0
    while index_counter < len(sequence):
        current_entity = sequence[index_counter]
        if isinstance(current_entity, int):
            filtered_result.append(current_entity)
        index_counter += 1
    return filtered_result