from typing import List, Tuple

def get_row(two_dimensional_list: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    found_positions: List[Tuple[int, int]] = []
    outer_index: int = 0

    while outer_index < len(two_dimensional_list):
        inner_index: int = 0
        while inner_index < len(two_dimensional_list[outer_index]):
            if two_dimensional_list[outer_index][inner_index] == target_integer:
                found_positions.append((outer_index, inner_index))
            inner_index += 1
        outer_index += 1

    # Sort by inner_index descending, then by outer_index ascending
    found_positions.sort(key=lambda x: x[1], reverse=True)
    found_positions.sort(key=lambda x: x[0])
    return found_positions