from typing import List, Tuple

def get_row(two_dimensional_list: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    positions: List[Tuple[int, int]] = []
    primary_index: int = 0
    while primary_index < len(two_dimensional_list):
        secondary_index: int = 0
        while secondary_index < len(two_dimensional_list[primary_index]):
            if two_dimensional_list[primary_index][secondary_index] == target_integer:
                positions.append((primary_index, secondary_index))
            secondary_index += 1
        primary_index += 1
    # Sort by x ascending, then y descending
    positions.sort(key=lambda xy: (-xy[1]))
    positions.sort(key=lambda xy: xy[0])
    return positions