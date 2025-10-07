from typing import List, Any

def filter_integers(list_of_values: List[Any]) -> List[int]:
    output_sequence: List[int] = []
    index_counter: int = 0
    while index_counter < len(list_of_values):
        current_entity = list_of_values[index_counter]
        if isinstance(current_entity, int):
            output_sequence.append(current_entity)
        index_counter += 1
    return output_sequence