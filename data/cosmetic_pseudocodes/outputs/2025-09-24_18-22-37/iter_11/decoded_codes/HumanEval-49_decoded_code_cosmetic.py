def modp(integer_n: int, integer_p: int) -> int:
    accumulator: int = 1
    iteration_counter: int = 0
    while iteration_counter < integer_n:
        temp_multiplication = accumulator * 2
        accumulator = temp_multiplication - (temp_multiplication // integer_p) * integer_p
        iteration_counter += 1
    return accumulator