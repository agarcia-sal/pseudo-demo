from typing import List, Tuple, Dict, Set

def get_row(two_dimensional_list: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    found_positions: Dict[int, Set[int]] = {}
    row_counter: int = 0
    while row_counter < len(two_dimensional_list):
        col_counter: int = 0
        while col_counter < len(two_dimensional_list[row_counter]):
            if two_dimensional_list[row_counter][col_counter] == target_integer:
                if row_counter in found_positions:
                    found_positions[row_counter].add(col_counter)
                else:
                    found_positions[row_counter] = {col_counter}
            col_counter += 1
        row_counter += 1

    result_list: List[Tuple[int, int]] = []
    for row_key in sorted(found_positions.keys()):
        for col_value in sorted(found_positions[row_key], reverse=True):
            result_list.append((row_key, col_value))

    return result_list