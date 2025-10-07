from typing import List, Union

def median(list_of_elements: List[Union[int, float]]) -> float:
    sorted_array = sorted(list_of_elements)
    total_items = len(sorted_array)
    middle_pos = total_items // 2

    if total_items % 2 != 0:
        return float(sorted_array[middle_pos])
    else:
        left_mid = sorted_array[middle_pos - 1]
        right_mid = sorted_array[middle_pos]
        return (left_mid + right_mid) / 2.0