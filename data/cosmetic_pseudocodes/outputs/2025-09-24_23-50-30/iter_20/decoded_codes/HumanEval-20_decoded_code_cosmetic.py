from typing import Sequence, Optional, List, Tuple

def find_closest_elements(input_sequence: Sequence[int]) -> Optional[List[int]]:
    result_pair: Optional[List[int]] = None
    current_min: Optional[int] = None

    def def_inner_loop(
        a_index: int,
        a_value: int,
        remaining_index: int,
        remaining_value_list: Sequence[int],
        cur_min: Optional[int],
        cur_pair: Optional[List[int]],
    ) -> Tuple[Optional[List[int]], Optional[int]]:
        if remaining_index >= len(input_sequence):
            return cur_pair, cur_min
        b_value = remaining_value_list[0]
        b_index = remaining_index
        updated_pair, updated_min = cur_pair, cur_min
        if a_index != b_index:
            dist_calc = b_value - a_value
            dist_abs = dist_calc if dist_calc >= 0 else -dist_calc
            if updated_min is None or dist_abs < updated_min:
                updated_min = dist_abs
                updated_pair = [a_value, b_value]
                if updated_pair[0] > updated_pair[1]:
                    updated_pair[0], updated_pair[1] = updated_pair[1], updated_pair[0]
        return def_inner_loop(a_index, a_value, b_index + 1, remaining_value_list[1:], updated_min, updated_pair)

    def def_outer_loop(
        outer_index: int,
        remaining_list: Sequence[int],
        cur_min: Optional[int],
        cur_pair: Optional[List[int]],
    ) -> Optional[List[int]]:
        if outer_index >= len(input_sequence):
            return cur_pair
        curr_val = remaining_list[0]
        pair_after_inner, min_after_inner = def_inner_loop(outer_index, curr_val, 0, input_sequence, cur_min, cur_pair)
        return def_outer_loop(outer_index + 1, remaining_list[1:], min_after_inner, pair_after_inner)

    return def_outer_loop(0, input_sequence, current_min, result_pair)