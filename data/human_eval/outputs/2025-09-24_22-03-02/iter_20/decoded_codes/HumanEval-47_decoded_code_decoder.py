from typing import List, Union

def median(l: List[Union[int, float]]) -> Union[int, float]:
    l = sorted(l)
    n = len(l)
    if n % 2 == 1:
        index = n // 2
        return l[index]
    else:
        left_index = n // 2 - 1
        right_index = n // 2
        left_value = l[left_index]
        right_value = l[right_index]
        sum_values = left_value + right_value
        median_value = sum_values / 2.0
        return median_value