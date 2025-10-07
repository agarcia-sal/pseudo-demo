from typing import List

def rescale_to_unit(array_of_values: List[float]) -> List[float]:
    base_val: float = float('inf')
    peak_val: float = float('-inf')
    index_var: int = 0

    while index_var < len(array_of_values):
        val = array_of_values[index_var]
        if val < base_val:
            base_val = val
        if val > peak_val:
            peak_val = val
        index_var += 1

    normalized_list: List[float] = []
    counter_var: int = 0

    while counter_var < len(array_of_values):
        diff_val = array_of_values[counter_var] - base_val
        range_span = peak_val - base_val
        scaled_val = diff_val / range_span if range_span != 0 else 0.0
        normalized_list.append(scaled_val)
        counter_var += 1

    return normalized_list