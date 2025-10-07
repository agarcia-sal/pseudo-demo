from typing import Sequence, Optional

def next_smallest(sequence: Sequence[int]) -> Optional[int]:
    temp_map: dict[int, bool] = {}
    for element in sequence:
        temp_map[element] = True
    unique_collection = sorted(temp_map.keys())
    result: Optional[int] = None
    if len(unique_collection) >= 2:
        result = unique_collection[1]
    return result