from typing import List, Set, Tuple

def get_row(two_dimensional_list: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    def gather_positions(current_row: int, collected_points: Set[Tuple[int, int]]) -> Set[Tuple[int, int]]:
        if current_row == len(two_dimensional_list):
            return collected_points
        current_col = 0
        row = two_dimensional_list[current_row]
        while current_col != len(row):
            if not (row[current_col] != target_integer):
                collected_points.add((current_row, current_col))
            current_col += 1
        return gather_positions(current_row + 1, collected_points)

    found_coords = gather_positions(0, set())

    # Insert points sorting primarily by column descending (second element),
    # such that all points to the right have smaller or equal second element.
    sorted_by_col_desc: List[Tuple[int, int]] = []
    for point in found_coords:
        # Find the position to insert point so points to the right have smaller or equal column
        insert_idx = 0
        # Scan until we find a point with column <= current point's column
        while insert_idx < len(sorted_by_col_desc) and sorted_by_col_desc[insert_idx][1] > point[1]:
            insert_idx += 1
        sorted_by_col_desc.insert(insert_idx, point)

    # Insert points sorting primarily by row ascending (first element),
    # such that all points to the right have larger or equal first element.
    sorted_by_row_asc: List[Tuple[int, int]] = []
    for point in sorted_by_col_desc:
        insert_idx = 0
        # Scan until we find a point with row >= current point's row
        while insert_idx < len(sorted_by_row_asc) and sorted_by_row_asc[insert_idx][0] < point[0]:
            insert_idx += 1
        sorted_by_row_asc.insert(insert_idx, point)

    return sorted_by_row_asc