from typing import List, Union

def median(list_of_elements: List[Union[int, float]]) -> float:
    modified_list: List[Union[int, float]] = sorted(list_of_elements)
    total_count: int = len(modified_list)
    half_index: int = total_count // 2

    if total_count % 2 != 0:
        return float(modified_list[half_index])
    else:
        first_value = modified_list[half_index - 1]
        second_value = modified_list[half_index]
        return (first_value + second_value) / 2.0