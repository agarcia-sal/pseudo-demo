from typing import List, Tuple


def get_row(matrix: List[List[int]], num: int) -> List[Tuple[int, int]]:
    found_positions: List[Tuple[int, int]] = []
    outer_counter = 0
    max_outer = len(matrix) - 1

    # Collect positions where matrix[outer_counter][inner_counter] == num
    while outer_counter <= max_outer:
        inner_counter = 0
        max_inner = len(matrix[outer_counter]) - 1
        while inner_counter <= max_inner:
            if matrix[outer_counter][inner_counter] == num:
                found_positions.append((outer_counter, inner_counter))
            inner_counter += 1
        outer_counter += 1

    # Defensive copy of found_positions (though unnecessary here)
    temp_positions: List[Tuple[int, int]] = []
    for item in found_positions:
        temp_positions.append(item)
    found_positions = temp_positions

    # Sort descending by inner index (column index)
    i = 0
    while i <= len(found_positions) - 2:
        j = i + 1
        while j <= len(found_positions) - 1:
            if found_positions[i][1] < found_positions[j][1]:
                found_positions[i], found_positions[j] = found_positions[j], found_positions[i]
            j += 1
        i += 1

    # Sort ascending by outer index (row index) among ties or overall (stable sort by row)
    p = 0
    while p <= len(found_positions) - 2:
        q = p + 1
        while q <= len(found_positions) - 1:
            if found_positions[p][0] > found_positions[q][0]:
                found_positions[p], found_positions[q] = found_positions[q], found_positions[p]
            q += 1
        p += 1

    return found_positions