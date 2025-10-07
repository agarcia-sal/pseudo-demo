def starts_one_ends(num: int) -> int:
    if num == 1:
        return 1
    else:
        exponent = num - 2
        base_value = 10
        power_result = base_value ** exponent
        return 18 * power_result