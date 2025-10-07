from typing import List


def fizz_buzz(param_x: int) -> int:
    container_v: List[int] = []
    index_m = 0
    while index_m < param_x:
        condition_a = (index_m % 11) == 0
        condition_b = (index_m % 13) == 0
        if condition_a or condition_b:
            container_v.append(index_m)
        index_m += 1
    aggregate_s = ""
    position_z = 0
    while position_z < len(container_v):
        element_q = container_v[position_z]
        aggregate_s += str(element_q)
        position_z += 1
    accumulator_r = 0
    for pos_c in range(1, len(aggregate_s) + 1):
        current_char = aggregate_s[pos_c - 1]
        if current_char == '7':
            accumulator_r += 1
    return accumulator_r