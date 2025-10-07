def sum_to_n(var_x: int) -> int:
    var_total: int = 0
    var_i: int = 0
    while var_i <= var_x:
        var_total += var_i
        var_i += 1
    return var_total