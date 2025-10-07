from typing import List, Union

def median(list_of_elements: List[Union[int, float]]) -> Union[int, float]:
    ordered_elements: List[Union[int, float]] = sorted(list_of_elements)
    count_elements: int = len(ordered_elements)

    if count_elements % 2 != 0:
        middle_index: int = count_elements // 2
        return ordered_elements[middle_index]
    else:
        upper_mid: int = count_elements // 2
        lower_mid: int = upper_mid - 1
        sum_of_mids: Union[int, float] = ordered_elements[lower_mid] + ordered_elements[upper_mid]
        return sum_of_mids / 2.0