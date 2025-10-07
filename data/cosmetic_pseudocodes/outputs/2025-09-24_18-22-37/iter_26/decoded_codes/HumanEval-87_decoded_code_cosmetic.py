from typing import List, Tuple

def get_row(two_dimensional_list: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    collected_positions: List[Tuple[int, int]] = []
    outer_pos: int = 0
    while outer_pos < len(two_dimensional_list):
        inner_pos: int = 0
        current_row = two_dimensional_list[outer_pos]
        while inner_pos < len(current_row):
            current_item = current_row[inner_pos]
            if current_item == target_integer:
                collected_positions.append((outer_pos, inner_pos))
            inner_pos += 1
        outer_pos += 1

    # First sort by column descending
    temp_sorted_by_column = sorted(collected_positions, key=lambda p: p[1], reverse=True)
    # Then sort by row ascending, stable sort preserves previous ordering for same rows
    fully_sorted_positions = sorted(temp_sorted_by_column, key=lambda p: p[0])

    return fully_sorted_positions