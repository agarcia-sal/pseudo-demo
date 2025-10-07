def modp(integer_n: int, integer_p: int) -> int:
    var_i: int = 0
    var_r: int = 1
    while var_i < integer_n:
        var_r = (var_r * 2) - (integer_p * ((var_r * 2) // integer_p))
        var_i += 1
    return var_r