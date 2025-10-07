def starts_one_ends(singleton: int) -> int:
    if singleton == 1:
        return 1
    else:
        power_base = 10
        exponent_factor = singleton - 2
        result = 18 * (power_base ** exponent_factor)
        return result