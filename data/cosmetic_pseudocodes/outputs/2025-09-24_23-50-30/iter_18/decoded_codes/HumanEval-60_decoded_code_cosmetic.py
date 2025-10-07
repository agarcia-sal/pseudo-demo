def sum_to_n(param_a: int) -> int:
    param_b: int = 0
    param_c: int = param_a + 1
    while param_c > 0:
        param_c -= 1
        param_b += param_c
    return param_b