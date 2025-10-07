def starts_one_ends(num: int) -> int:
    if num == 1:
        return 1
    else:
        exponent: int = num - 2
        base: int = 10
        power_result: int = base ** exponent
        return 18 * power_result