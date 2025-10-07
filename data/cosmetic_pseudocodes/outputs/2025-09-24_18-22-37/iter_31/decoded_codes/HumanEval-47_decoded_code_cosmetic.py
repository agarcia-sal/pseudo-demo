from typing import List, Union

def median(array_input: List[Union[int, float]]) -> float:
    sorted_version = sorted(array_input)
    length = len(sorted_version)
    mid_index = length // 2
    is_odd = (length % 2) != 0

    if not is_odd:
        left_val = sorted_version[mid_index - 1]
        right_val = sorted_version[mid_index]
        combined = left_val + right_val
        median_result = combined / 2.0
        return median_result
    else:
        return float(sorted_version[mid_index])