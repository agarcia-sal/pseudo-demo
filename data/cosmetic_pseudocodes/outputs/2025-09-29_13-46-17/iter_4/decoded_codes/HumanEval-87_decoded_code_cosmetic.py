from typing import List, Tuple

def get_row(two_dimensional_list: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    def collect_inner(idx_inner: int, current_row: List[int], acc_inner: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        if idx_inner >= len(current_row):
            return acc_inner
        if current_row[idx_inner] == target_integer:
            return collect_inner(idx_inner + 1, current_row, acc_inner + [(idx_outer, idx_inner)])
        return collect_inner(idx_inner + 1, current_row, acc_inner)

    def collect_positions(idx_outer: int, acc_positions: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        if idx_outer >= len(two_dimensional_list):
            return acc_positions
        updated_positions = collect_inner(0, two_dimensional_list[idx_outer], acc_positions)
        return collect_positions(idx_outer + 1, updated_positions)

    found_coords = collect_positions(0, [])

    # Sort by column descending (second element descending)
    sorted_by_col_desc = sorted(found_coords, key=lambda x: x[1], reverse=True)
    # Then sort by row ascending (first element ascending)
    fully_sorted = sorted(sorted_by_col_desc, key=lambda x: x[0])
    return fully_sorted