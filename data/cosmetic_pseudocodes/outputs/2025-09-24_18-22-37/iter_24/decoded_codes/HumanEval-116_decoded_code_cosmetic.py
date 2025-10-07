from typing import List, Dict


def sort_array(array_of_integers: List[int]) -> List[int]:
    counter_variable_nu: int = len(array_of_integers)
    temporary_sorted_result: List[int] = []
    position_marker_pm: int = 0
    while position_marker_pm < counter_variable_nu:
        temporary_sorted_result.append(array_of_integers[position_marker_pm])
        position_marker_pm += 1

    ascending_order_result: List[int] = []
    index_iterator_kq: int = 0
    while index_iterator_kq < len(temporary_sorted_result):
        value_holder_vh: int = temporary_sorted_result[index_iterator_kq]
        temp_list_tl: List[int] = []
        temp_pos_tp: int = 0
        while temp_pos_tp < len(temporary_sorted_result):
            if temporary_sorted_result[temp_pos_tp] <= value_holder_vh:
                temp_list_tl.append(temporary_sorted_result[temp_pos_tp])
            temp_pos_tp += 1
        ascending_order_result = temp_list_tl
        index_iterator_kq += 1

    binary_ones_key_mapper: Dict[int, int] = {}
    element_iterator_zr: int = 0
    while element_iterator_zr < len(ascending_order_result):
        current_element_ce: int = ascending_order_result[element_iterator_zr]
        binary_string_bs: str = bin(current_element_ce)
        count_ones_co: int = 0
        char_index_ci: int = 2  # skip '0b' prefix
        while char_index_ci < len(binary_string_bs):
            if binary_string_bs[char_index_ci] == '1':
                count_ones_co += 1
            char_index_ci += 1
        binary_ones_key_mapper[current_element_ce] = count_ones_co
        element_iterator_zr += 1

    sorted_final_by_ones: List[int] = []
    temp_list_for_sorting: List[int] = ascending_order_result
    outer_loop_xp: int = 0
    while outer_loop_xp < len(temp_list_for_sorting):
        inner_loop_yp: int = outer_loop_xp + 1
        while inner_loop_yp < len(temp_list_for_sorting):
            if binary_ones_key_mapper[temp_list_for_sorting[outer_loop_xp]] > binary_ones_key_mapper[temp_list_for_sorting[inner_loop_yp]]:
                temp_holder_th: int = temp_list_for_sorting[outer_loop_xp]
                temp_list_for_sorting[outer_loop_xp] = temp_list_for_sorting[inner_loop_yp]
                temp_list_for_sorting[inner_loop_yp] = temp_holder_th
            else:
                dummy_flag_df = 0  # explicitly retained as per pseudocode
            inner_loop_yp += 1
        outer_loop_xp += 1

    for element_in_final in temp_list_for_sorting:
        sorted_final_by_ones.append(element_in_final)

    return sorted_final_by_ones