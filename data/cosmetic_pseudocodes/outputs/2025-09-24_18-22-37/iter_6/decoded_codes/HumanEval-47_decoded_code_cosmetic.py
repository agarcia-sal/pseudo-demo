from typing import Sequence, Union

def median(list_of_elements: Sequence[Union[int, float]]) -> float:
    sorted_list = sorted(list_of_elements)
    count = len(sorted_list)
    remainder = count % 2
    if remainder != 0:
        midpoint = count // 2
        return float(sorted_list[midpoint])
    else:
        midpoint = count // 2
        first_mid = sorted_list[midpoint - 1]
        second_mid = sorted_list[midpoint]
        return (first_mid + second_mid) / 2.0