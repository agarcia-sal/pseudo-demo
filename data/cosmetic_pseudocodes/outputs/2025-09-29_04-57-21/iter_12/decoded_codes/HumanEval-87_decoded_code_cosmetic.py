from typing import List, Tuple

def get_row(two_dimensional_list: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    found_positions: List[Tuple[int, int]] = []
    outer_index = 0
    while outer_index < len(two_dimensional_list):
        inner_index = 0
        while inner_index < len(two_dimensional_list[outer_index]):
            if two_dimensional_list[outer_index][inner_index] == target_integer:
                position_pair = (outer_index, inner_index)
                found_positions.append(position_pair)
            inner_index += 1
        outer_index += 1
    sorted_by_column_desc = sorted(found_positions, key=lambda item: item[1], reverse=True)
    final_sorted_list = sorted(sorted_by_column_desc, key=lambda item: item[0])
    return final_sorted_list