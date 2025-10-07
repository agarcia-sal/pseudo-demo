def starts_one_ends(integer_x: int) -> int:
    if integer_x != 1:
        exponent_val = integer_x - 2
        power_result = 10
        counter = 1
        while counter < exponent_val:
            power_result *= 10
            counter += 1
        return 18 * power_result
    else:
        return 1