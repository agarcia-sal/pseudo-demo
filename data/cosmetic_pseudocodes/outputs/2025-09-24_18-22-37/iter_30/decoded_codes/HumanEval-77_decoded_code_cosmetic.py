def iscube(param_x: int) -> bool:
    var_a: int = -param_x if param_x < 0 else param_x
    var_b: int = round(var_a ** (1/3))
    var_c: int = var_b * var_b * var_b
    return var_c == var_a