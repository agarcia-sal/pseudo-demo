from typing import List


def modp(integer_n: int, integer_p: int) -> int:
    stack_list: List[int] = [integer_n]
    accumulator: int = 1
    while len(stack_list) > 0:
        current_corr: int = stack_list[0]
        stack_list = stack_list[1:]
        if current_corr > 0:
            new_accum: int = accumulator
            doubled_val: int = new_accum + new_accum
            modded_val: int = doubled_val - ((doubled_val // integer_p) * integer_p)
            accumulator = modded_val
            stack_list = [current_corr - 1] + stack_list
    return accumulator