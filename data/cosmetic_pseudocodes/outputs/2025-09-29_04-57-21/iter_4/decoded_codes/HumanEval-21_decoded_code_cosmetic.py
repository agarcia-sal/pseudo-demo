from typing import List

def rescale_to_unit(input_array: List[float]) -> List[float]:
    lowest_val: float = float('inf')
    highest_val: float = float('-inf')
    idx: int = 0

    while idx < len(input_array):
        val = input_array[idx]
        if val < lowest_val:
            lowest_val = val
        if val > highest_val:
            highest_val = val
        idx += 1

    scale_factor: float = highest_val - lowest_val
    # Handle edge case: all values are equal (scale_factor == 0)
    if scale_factor == 0:
        return [0.0 for _ in input_array]

    output_list: List[float] = []
    iterator: int = 0
    while iterator < len(input_array):
        output_list.append((input_array[iterator] - lowest_val) / scale_factor)
        iterator += 1

    return output_list