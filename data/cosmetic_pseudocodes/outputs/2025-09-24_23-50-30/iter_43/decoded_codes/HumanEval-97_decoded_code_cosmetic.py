from typing import List


def multiply(param_x: int, param_y: int) -> int:
    temp_arr: List[int] = [param_x % 10, param_y % 10]
    idx: int = 0
    prod_val: int = 1

    while idx <= 1:
        val: int = temp_arr[idx]
        # Multiply by absolute value of val
        prod_val *= (val if val >= 0 else -val)
        idx += 1

    return prod_val