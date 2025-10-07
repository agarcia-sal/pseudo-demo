from typing import List, Tuple, Dict


def get_row(two_dimensional_list: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    def find_positions(r: int, c: int, acc: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        if r < 0:
            return acc
        if c < 0:
            return find_positions(r - 1, len(two_dimensional_list[r - 1]) - 1, acc)
        if two_dimensional_list[r][c] != target_integer:
            return find_positions(r, c - 1, acc)
        return find_positions(r, c - 1, [(r, c)] + acc)

    total_rows = len(two_dimensional_list)
    initial_col = len(two_dimensional_list[total_rows - 1]) - 1 if total_rows > 0 else -1
    found_coords = find_positions(total_rows - 1, initial_col, [])
    grouped_by_row: Dict[int, List[int]] = {}
    for r, c in found_coords:
        if r not in grouped_by_row:
            grouped_by_row[r] = []
        grouped_by_row[r] = [c] + grouped_by_row[r]

    sorted_rows = sorted(grouped_by_row.keys())
    final_result: List[Tuple[int, int]] = []
    for r_key in sorted_rows:
        sorted_cols_desc = sorted(grouped_by_row[r_key], reverse=True)
        for c_val in sorted_cols_desc:
            final_result.append((r_key, c_val))
    return final_result