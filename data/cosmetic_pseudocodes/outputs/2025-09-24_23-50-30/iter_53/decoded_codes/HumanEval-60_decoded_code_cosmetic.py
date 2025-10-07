def sum_to_n(param_a: int) -> int:
    param_b: int = 0
    param_c: int = 0
    while param_c <= param_a:
        param_b += param_c
        param_c += 1
    return param_b