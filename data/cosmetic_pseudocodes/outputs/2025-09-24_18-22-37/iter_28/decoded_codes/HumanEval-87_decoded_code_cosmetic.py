from typing import List, Tuple, Any

def get_row(lst_2d: List[List[Any]], val_target: Any) -> List[Tuple[int, int]]:
    found_positions: List[Tuple[int, int]] = []
    i_counter: int = 0
    while i_counter <= len(lst_2d) - 1:
        j_counter: int = 0
        while j_counter <= len(lst_2d[i_counter]) - 1:
            current_element = lst_2d[i_counter][j_counter]
            condition_flag = (current_element == val_target)
            if not condition_flag:
                skip_addition = True
            else:
                skip_addition = False
            if not skip_addition:
                pos_pair = (i_counter, j_counter)
                found_positions.append(pos_pair)
            j_counter += 1
        i_counter += 1

    sorted_by_col_desc: List[Tuple[int, int]] = []
    index_c: int = 0
    while index_c < len(found_positions):
        sorted_by_col_desc = sorted_by_col_desc + [found_positions[index_c]]
        index_c += 1

    flag_swap: bool = True
    while flag_swap:
        flag_swap = False
        idx_p: int = 0
        while idx_p < len(sorted_by_col_desc) - 1:
            if sorted_by_col_desc[idx_p][1] < sorted_by_col_desc[idx_p + 1][1]:
                temp_swap = sorted_by_col_desc[idx_p]
                sorted_by_col_desc[idx_p] = sorted_by_col_desc[idx_p + 1]
                sorted_by_col_desc[idx_p + 1] = temp_swap
                flag_swap = True
            idx_p += 1

    sorted_by_row_asc: List[Tuple[int, int]] = []
    counter_z: int = 0
    while counter_z < len(sorted_by_col_desc):
        sorted_by_row_asc = sorted_by_row_asc + [sorted_by_col_desc[counter_z]]
        counter_z += 1

    flag_sorted: bool = True
    while flag_sorted:
        flag_sorted = False
        idx_r: int = 0
        while idx_r < len(sorted_by_row_asc) - 1:
            if sorted_by_row_asc[idx_r][0] > sorted_by_row_asc[idx_r + 1][0]:
                temp_swap = sorted_by_row_asc[idx_r]
                sorted_by_row_asc[idx_r] = sorted_by_row_asc[idx_r + 1]
                sorted_by_row_asc[idx_r + 1] = temp_swap
                flag_sorted = True
            idx_r += 1

    return sorted_by_row_asc