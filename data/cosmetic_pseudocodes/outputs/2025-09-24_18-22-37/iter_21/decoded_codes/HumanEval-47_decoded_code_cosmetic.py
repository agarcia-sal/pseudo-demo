from typing import List, Union


def median(list_of_elements: List[Union[int, float]]) -> float:
    various_index: int = 0
    local_sorted: List[Union[int, float]] = list_of_elements.copy()

    local_sorted = sorted(local_sorted)
    length_var: int = len(local_sorted)

    if length_var % 2 != 0:
        various_index = (length_var - 1) // 2  # integer division for index
        return float(local_sorted[various_index])
    else:
        var_right = length_var // 2
        var_left = var_right - 1

        left_value = local_sorted[var_left]
        right_value = local_sorted[var_right]

        average = (left_value + right_value) / 2.0
        return average