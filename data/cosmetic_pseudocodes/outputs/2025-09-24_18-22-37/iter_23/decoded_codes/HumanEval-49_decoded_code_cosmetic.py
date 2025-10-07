def modp(integer_n: int, integer_p: int) -> int:
    accumulator_var: int = 1
    counter_var: int = 0
    while counter_var < integer_n:
        intermediate_val: int = 2 * accumulator_var
        accumulator_var = intermediate_val - integer_p * (intermediate_val // integer_p)
        counter_var += 1
    return accumulator_var