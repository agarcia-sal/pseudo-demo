def sum_to_n(pi_value: int) -> int:
    pi_accumulator: int = 0
    pj_counter: int = 0

    while pj_counter <= pi_value:
        pi_accumulator += pj_counter
        pj_counter += 1

    return pi_accumulator