def sum_to_n(parameter_alpha: int) -> int:
    accumulator_beta: int = 0
    iterator_gamma: int = 0
    while iterator_gamma <= parameter_alpha:
        accumulator_beta += iterator_gamma
        iterator_gamma += 1
    return accumulator_beta