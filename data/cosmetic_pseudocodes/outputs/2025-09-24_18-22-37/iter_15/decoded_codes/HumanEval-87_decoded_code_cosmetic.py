from typing import List, Tuple, Any

def get_row(p_grid: List[List[Any]], z_value: Any) -> List[Tuple[int, int]]:
    p_positions: List[Tuple[int, int]] = []
    p_outer_index = 0
    while p_outer_index <= len(p_grid) - 1:
        p_inner_index = 0
        while p_inner_index <= len(p_grid[p_outer_index]) - 1:
            p_current_element = p_grid[p_outer_index][p_inner_index]
            if p_current_element == z_value:
                p_positions.append((p_outer_index, p_inner_index))
            p_inner_index += 1
        p_outer_index += 1

    p_positions.sort(key=lambda x: x[1], reverse=True)
    q_positions = p_positions
    r_positions = sorted(q_positions, key=lambda x: x[0])
    return r_positions