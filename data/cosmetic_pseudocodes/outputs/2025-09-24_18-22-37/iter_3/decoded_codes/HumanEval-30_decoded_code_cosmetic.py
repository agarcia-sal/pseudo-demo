from typing import List

def get_positive(input_array: List[int]) -> List[int]:
    idx: int = 0
    result_array: List[int] = []
    while idx < len(input_array):
        current: int = input_array[idx]
        if current > 0:
            result_array.append(current)
        idx += 1
    return result_array