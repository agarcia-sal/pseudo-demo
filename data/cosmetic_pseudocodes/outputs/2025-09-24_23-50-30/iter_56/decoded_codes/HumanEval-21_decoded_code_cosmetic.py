from typing import List


def rescale_to_unit(array_of_values: List[float]) -> List[float]:
    idx_a: int = 0
    temp_min: float = array_of_values[0]
    temp_max: float = array_of_values[0]

    while idx_a < len(array_of_values):
        # Update temp_min if current value is less
        temp_min = temp_min if temp_min <= array_of_values[idx_a] else array_of_values[idx_a]
        # Update temp_max if current value is greater
        temp_max = temp_max if temp_max >= array_of_values[idx_a] else array_of_values[idx_a]
        idx_a += 1

    def aux_collect(idx_b: int, acc_list: List[float]) -> List[float]:
        if idx_b < len(array_of_values):
            diff_value = array_of_values[idx_b] - temp_min
            denom_value = temp_max - temp_min
            # Handle division by zero if all values are equal
            scaled = diff_value / denom_value if denom_value != 0 else 0.0
            return aux_collect(idx_b + 1, acc_list + [scaled])
        else:
            return acc_list

    return aux_collect(0, [])