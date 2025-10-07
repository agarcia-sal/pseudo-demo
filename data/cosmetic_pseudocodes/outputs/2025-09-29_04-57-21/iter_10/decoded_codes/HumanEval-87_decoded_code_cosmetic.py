from typing import List, Tuple

def get_row(two_dimensional_list: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    found_positions: List[Tuple[int, int]] = []
    outer_index = 0
    while outer_index < len(two_dimensional_list):
        inner_index = 0
        while inner_index < len(two_dimensional_list[outer_index]):
            if two_dimensional_list[outer_index][inner_index] == target_integer:
                found_positions.append((outer_index, inner_index))
            inner_index += 1
        outer_index += 1

    # Insert into temp_positions ordered by inner index descending
    temp_positions: List[Tuple[int, int]] = []
    for coord in found_positions:
        inserted = False
        for i, existing in enumerate(temp_positions):
            if coord[1] > existing[1]:
                temp_positions.insert(i, coord)
                inserted = True
                break
        if not inserted:
            temp_positions.append(coord)

    # Insert into sorted_positions ordered by outer index ascending
    sorted_positions: List[Tuple[int, int]] = []
    for coord in temp_positions:
        inserted = False
        for i, existing in enumerate(sorted_positions):
            if coord[0] < existing[0]:
                sorted_positions.insert(i, coord)
                inserted = True
                break
        if not inserted:
            sorted_positions.append(coord)

    return sorted_positions