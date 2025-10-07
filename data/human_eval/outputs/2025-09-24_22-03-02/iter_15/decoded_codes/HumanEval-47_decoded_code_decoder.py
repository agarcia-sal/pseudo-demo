from typing import List, Union

def median(l: List[Union[int, float]]) -> Union[int, float]:
    l = sorted(l)
    if len(l) % 2 == 1:
        middle_index = len(l) // 2
        return l[middle_index]
    else:
        middle_left_index = (len(l) // 2) - 1
        middle_right_index = len(l) // 2
        sum_middle_elements = l[middle_left_index] + l[middle_right_index]
        return sum_middle_elements / 2.0