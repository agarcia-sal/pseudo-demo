def modp(integer_alpha: int, integer_beta: int) -> int:
    variable_gamma = 1
    variable_delta = 0
    while variable_delta < integer_alpha:
        variable_gamma = (variable_gamma * 2) % integer_beta
        variable_delta += 1
    return variable_gamma