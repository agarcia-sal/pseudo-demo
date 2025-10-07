def starts_one_ends(integer_n: int) -> int:
    if integer_n == 1:
        return 1
    else:
        base_value: int = 10
        exponent_value: int = integer_n - 2
        power_result: int = base_value ** exponent_value
        result: int = 18 * power_result
        return result