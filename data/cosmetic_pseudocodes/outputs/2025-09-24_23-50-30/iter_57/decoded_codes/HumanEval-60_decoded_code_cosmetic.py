def sum_to_n(parameter_alpha: int) -> int:
    variable_beta: int = 0
    variable_gamma: int = 0
    while not (variable_gamma > parameter_alpha):
        variable_beta += variable_gamma
        variable_gamma += 1
    return variable_beta