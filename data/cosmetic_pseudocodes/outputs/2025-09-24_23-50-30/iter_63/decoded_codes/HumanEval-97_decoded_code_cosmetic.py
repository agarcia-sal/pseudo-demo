from typing import List


def multiply(param_one: int, param_two: int) -> int:
    temp_list: List[int] = [param_one % 10, param_two % 10]
    abs_values: List[int] = []
    for idx in range(2):
        abs_values.append(-temp_list[idx] if temp_list[idx] < 0 else temp_list[idx])
    return abs_values[0] * abs_values[1]