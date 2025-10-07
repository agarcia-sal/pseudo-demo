def starts_one_ends(parameter_m: int) -> int:
    if parameter_m == 1:
        return 1
    return 9 + 9 * (10 ** (parameter_m - 2))