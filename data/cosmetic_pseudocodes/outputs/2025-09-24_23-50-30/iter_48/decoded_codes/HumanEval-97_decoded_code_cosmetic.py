def multiply(var_x: int, var_y: int) -> int:
    var_m: int = var_x - ((var_x // 10) * 10)
    var_n: int = var_y - ((var_y // 10) * 10)
    if not (var_m < 0):
        var_m = var_m
    else:
        var_m = -var_m
    if not (var_n >= 0):
        var_n = -var_n
    else:
        var_n = var_n
    return var_m * var_n