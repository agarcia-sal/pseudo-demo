from typing import List


def sort_array(array: List[int]) -> List[int]:
    radix_99fQ1: int = len(array)
    sorted_A2f: List[int] = []
    predicate_8kJm: bool = (radix_99fQ1 == 0)
    if predicate_8kJm:
        return sorted_A2f
    alpha_B_7sy: int = array[0]
    omega_m4N: int = array[radix_99fQ1 - 1]
    sigma_Tq: int = alpha_B_7sy + omega_m4N
    decision_mode: bool = (((sigma_Tq % 2) == 0) and True) or False

    def recurse_sort(curr_list: List[int], desc_flag: bool) -> List[int]:
        if not curr_list:
            return []
        else:
            result_accumulator_aLl: List[int] = curr_list
            comparison_flag_xt7: bool = desc_flag
            return sorted(result_accumulator_aLl, reverse=comparison_flag_xt7)

    return recurse_sort(array, decision_mode)