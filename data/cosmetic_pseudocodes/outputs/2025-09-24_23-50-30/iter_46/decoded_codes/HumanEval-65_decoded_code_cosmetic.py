def circular_shift(param_a: object, param_b: int) -> str:
    var_p: str = str(param_a)
    if not (param_b <= len(var_p)):
        return var_p[::-1]
    var_m: int = len(var_p) - param_b
    var_c: str = var_p[var_m:]
    var_d: str = var_p[:var_m]
    return var_c + var_d