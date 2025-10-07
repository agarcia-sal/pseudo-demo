from typing import List, Optional, Sequence

def intersperse(number_collection: Optional[Sequence[int]], separator: int) -> List[int]:
    if not number_collection or len(number_collection) == 0:
        return []
    accumulated_sequence: List[int] = []
    iterator_index = 0
    while iterator_index < len(number_collection) - 1:
        current_item = number_collection[iterator_index]
        accumulated_sequence.append(current_item)
        accumulated_sequence.append(separator)
        iterator_index += 1
    accumulated_sequence.append(number_collection[-1])
    return accumulated_sequence