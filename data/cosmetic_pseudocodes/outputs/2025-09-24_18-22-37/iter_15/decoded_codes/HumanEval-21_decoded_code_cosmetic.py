from typing import List

def rescale_to_unit(array_of_values: List[float]) -> List[float]:
    if not array_of_values:
        return []
    tmp_min: float = array_of_values[0]
    tmp_max: float = array_of_values[0]
    for value in array_of_values:
        if value < tmp_min:
            tmp_min = value
        if value > tmp_max:
            tmp_max = value
    delta = tmp_max - tmp_min
    if delta == 0.0:
        return [0.0 for _ in array_of_values]
    result_array: List[float] = []
    for value in array_of_values:
        numerator = value - tmp_min
        scaled_value = numerator / delta
        result_array.append(scaled_value)
    return result_array