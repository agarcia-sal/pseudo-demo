from typing import List, Tuple

def get_row(matrix_data: List[List[int]], search_value: int) -> List[Tuple[int, int]]:
    result_coords: List[Tuple[int, int]] = []
    outer_idx: int = 0
    while outer_idx < len(matrix_data):
        inner_idx: int = 0
        while inner_idx < len(matrix_data[outer_idx]):
            current_element: int = matrix_data[outer_idx][inner_idx]
            if current_element == search_value:
                coord_pair = (outer_idx, inner_idx)
                result_coords.append(coord_pair)
            inner_idx += 1  # 1 + 0 simplified
        outer_idx += 1  # 1 + 0 simplified

    # Sort result_coords by row ascending, then by column descending within same row
    result_coords.sort(key=lambda a: (a[0], -a[1]))

    # Then sort by row ascending again (redundant with previous, but preserved as per pseudocode)
    result_coords.sort(key=lambda x: x[0])

    return result_coords