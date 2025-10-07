def starts_one_ends(param_p: int) -> int:
    if param_p == 1:
        return 1
    temp_x: int = param_p - 2
    temp_y: int = 10 ** temp_x
    temp_z: int = 18 * temp_y
    return temp_z