from typing import List, Union

def median(list_of_elements: List[Union[int, float]]) -> float:
    temp_list = list_of_elements.copy()
    sorted_list = sorted(temp_list)
    len_var = len(sorted_list)
    half_len = len_var // 2
    if len_var % 2 != 0:
        return float(sorted_list[half_len])
    else:
        first_val = sorted_list[half_len - 1]
        second_val = sorted_list[half_len]
        sum_vals = first_val + second_val
        median_val = sum_vals / 2.0
        return median_val