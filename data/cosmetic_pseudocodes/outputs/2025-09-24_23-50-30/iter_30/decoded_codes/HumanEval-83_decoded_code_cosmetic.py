def starts_one_ends(param_alpha: int) -> int:
    if param_alpha == 1:
        return 1
    else:
        return 9 + 9 * 10 ** (param_alpha + (-2))