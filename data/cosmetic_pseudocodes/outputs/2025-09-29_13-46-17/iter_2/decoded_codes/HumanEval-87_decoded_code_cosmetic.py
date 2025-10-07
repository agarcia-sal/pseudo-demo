from typing import List, Tuple

def get_row(two_dimensional_list: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    def gather_positions(idx_r: int, idx_c: int, coords_accum: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        if idx_r >= len(two_dimensional_list):
            return coords_accum
        if idx_c >= len(two_dimensional_list[idx_r]):
            return gather_positions(idx_r + 1, 0, coords_accum)
        current_value = two_dimensional_list[idx_r][idx_c]
        new_coords = coords_accum
        if not (current_value != target_integer):
            new_coords = coords_accum + [(idx_r, idx_c)]
        return gather_positions(idx_r, idx_c + 1, new_coords)

    found_positions = gather_positions(0, 0, [])

    # sort by column descending
    sorted_by_col_desc = sorted(found_positions, key=lambda x: x[1], reverse=True)
    # sort by row ascending; stable sort maintains previous order for equal keys
    sorted_by_row_asc = sorted(sorted_by_col_desc, key=lambda x: x[0])

    return sorted_by_row_asc