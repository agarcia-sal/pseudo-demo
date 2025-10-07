from typing import List, Optional

def prod_signs(input_list: List[int]) -> Optional[int]:
    if not input_list:
        return None

    if 0 in input_list:
        result_sign = 0
    else:
        neg_count = sum(1 for val in input_list if val < 0)
        result_sign = (-1) ** neg_count

    temp_abs_values: List[int] = [abs(input_list[i]) for i in range(1, len(input_list))]
    magnitude_sum = sum(temp_abs_values)

    return result_sign * magnitude_sum