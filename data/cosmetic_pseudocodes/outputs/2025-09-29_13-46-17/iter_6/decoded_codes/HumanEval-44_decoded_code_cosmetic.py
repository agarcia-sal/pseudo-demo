from typing import Callable

def change_base(integer_x: int, integer_base: int) -> str:
    def recurse_convert(accumulator_str: str, current_num: int) -> str:
        if current_num <= 0:
            return accumulator_str
        mod_digit = current_num % integer_base
        new_accumulator = str(mod_digit) + accumulator_str
        next_num = (current_num - mod_digit) // integer_base  # integer division
        return recurse_convert(new_accumulator, next_num)
    return recurse_convert("", integer_x)