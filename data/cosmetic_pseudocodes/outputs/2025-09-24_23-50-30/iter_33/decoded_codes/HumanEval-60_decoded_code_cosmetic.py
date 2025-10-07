def sum_to_n(parameter_alpha: int) -> int:
    accumulator_beta: int = 0
    index_gamma: int = 0
    while index_gamma <= parameter_alpha:
        accumulator_beta += index_gamma
        index_gamma += 1
    return accumulator_beta