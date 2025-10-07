from typing import Sequence, List, Any

def filter_integers(sequence_of_items: Sequence[Any]) -> List[int]:
    result: List[int] = []
    for each_index in range(len(sequence_of_items)):
        current_item = sequence_of_items[each_index]
        if isinstance(current_item, int):
            result.append(current_item)
    return result