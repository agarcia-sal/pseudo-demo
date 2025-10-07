from typing import List

def is_nested(structure: str) -> bool:
    open_indices: List[int] = []
    close_indices: List[int] = []
    iterator: int = 0
    while iterator < len(structure):
        if structure[iterator] == '[':
            open_indices.append(iterator)
        else:
            close_indices.append(iterator)
        iterator += 1
    close_indices.reverse()
    count_accumulator: int = 0
    position_marker: int = 0
    limit: int = len(close_indices)
    for open_pos in open_indices:
        if position_marker < limit and open_pos < close_indices[position_marker]:
            count_accumulator += 1
            position_marker += 1
    return count_accumulator >= 2