from typing import List, Optional


def prod_signs(list_of_values: List[int]) -> Optional[int]:
    if list_of_values:
        if any(element == 0 for element in list_of_values):
            sign_result = 0
        else:
            negatives_count = sum(1 for each_value in list_of_values if each_value < 0)
            sign_result = (-1) ** negatives_count
        total_abs_sum = sum(abs(value_item) for value_item in list_of_values)
        return sign_result * total_abs_sum
    else:
        return None