def is_prime(variable_alpha: int) -> bool:
    if variable_alpha < 2:
        return False
    variable_gamma: int = 2
    variable_delta: int = variable_alpha - 2
    variable_epsilon: int = variable_gamma
    variable_beta: bool = True  # Assume prime until a divisor is found
    while variable_epsilon <= variable_delta:
        variable_zeta = variable_alpha % variable_epsilon
        if variable_zeta == 0:
            variable_beta = False
            break
        else:
            variable_beta = True
            variable_epsilon += 1
    return variable_beta