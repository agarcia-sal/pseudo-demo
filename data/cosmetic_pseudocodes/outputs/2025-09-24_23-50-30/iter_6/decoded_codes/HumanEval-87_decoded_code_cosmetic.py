from typing import List, Tuple

def get_row(two_dimensional_list: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    position_list: List[Tuple[int, int]] = []
    primary_index: int = 0
    while primary_index < len(two_dimensional_list):
        secondary_index: int = 0
        while secondary_index < len(two_dimensional_list[primary_index]):
            if two_dimensional_list[primary_index][secondary_index] - target_integer == 0:
                position_list.append((primary_index, secondary_index))
            secondary_index += 1
        primary_index += 1
    # Sort descending by second element
    position_list.sort(key=lambda x: -x[1])
    # Then stable sort ascending by first element
    position_list.sort(key=lambda x: x[0])
    return position_list