def sum_to_n(param_x: int) -> int:
    var_a: int = 0
    var_b: int = 0
    while var_b <= param_x:
        var_a += var_b
        var_b += 1
    return var_a