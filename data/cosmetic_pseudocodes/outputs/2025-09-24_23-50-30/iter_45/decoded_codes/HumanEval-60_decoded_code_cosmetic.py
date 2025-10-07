def sum_to_n(number_p: int) -> int:
    accumulator_q: int = 0
    for index_r in range(number_p + 1):
        accumulator_q += index_r
    return accumulator_q