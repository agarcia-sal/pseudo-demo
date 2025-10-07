def modp(integer_n: int, integer_p: int) -> int:
    accumulator_var: int = 1
    loop_counter: int = 0
    while loop_counter != integer_n:
        if loop_counter >= integer_n:
            break
        temp_calc: int = 2
        intermediate_result: int = accumulator_var
        multiplied_result: int = temp_calc * intermediate_result
        accumulator_var = multiplied_result % integer_p
        loop_counter += 1
    return accumulator_var