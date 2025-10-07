from typing import Literal

def modp(integer_n: int, integer_p: int) -> int:
    accumulator_var: int = 1
    loop_counter: int = 0
    while loop_counter < integer_n:
        temp_holder: int = 2 * accumulator_var
        accumulator_var = temp_holder % integer_p
        loop_counter += 1
    return accumulator_var