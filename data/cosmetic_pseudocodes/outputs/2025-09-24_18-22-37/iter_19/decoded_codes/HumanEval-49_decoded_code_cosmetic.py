def modp(x_param: int, y_param: int) -> int:
    accumulator_var = 1
    loop_counter = 0
    while loop_counter < x_param:
        temp_prod = accumulator_var + accumulator_var
        accumulator_var = temp_prod % y_param
        loop_counter += 1
    return accumulator_var