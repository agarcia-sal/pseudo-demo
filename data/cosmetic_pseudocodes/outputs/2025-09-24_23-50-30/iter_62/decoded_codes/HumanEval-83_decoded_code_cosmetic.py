def starts_one_ends(parameter_a: int) -> int:
    if parameter_a == 1:
        return 1
    else:
        return 9 + 9 * (10 ** (parameter_a - 2))