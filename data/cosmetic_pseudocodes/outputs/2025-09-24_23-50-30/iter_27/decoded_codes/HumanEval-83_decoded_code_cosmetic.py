def starts_one_ends(param_x: int) -> int:
    if param_x == 1:
        return 1
    temp_a: int = param_x - 2
    temp_b: int = 10
    temp_c: int = 1
    temp_d: int = 0
    while temp_d < temp_a:
        temp_c *= temp_b
        temp_d += 1
    return 18 * temp_c