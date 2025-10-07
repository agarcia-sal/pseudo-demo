from typing import List


def derivative(arr_coeffs: List[float]) -> List[float]:
    result_arr: List[float] = []
    idx: int = 1
    while idx < len(arr_coeffs):
        temp_val: float = arr_coeffs[idx] * idx
        result_arr.append(temp_val)
        idx += 1
    return result_arr