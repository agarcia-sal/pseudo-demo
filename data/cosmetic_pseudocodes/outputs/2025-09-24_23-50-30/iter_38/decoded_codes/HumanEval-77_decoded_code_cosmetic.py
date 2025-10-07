def iscube(parameter_x: int) -> bool:
    variable_a: int = abs(parameter_x)
    variable_b: int = round(variable_a ** (1 / 3))
    variable_c: int = variable_b ** 3
    return variable_c == variable_a