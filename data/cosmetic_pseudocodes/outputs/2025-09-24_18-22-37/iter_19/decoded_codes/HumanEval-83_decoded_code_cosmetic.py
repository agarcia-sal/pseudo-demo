def starts_one_ends(integer_n: int) -> int:
    if integer_n == 1:
        temp_var = 1
    else:
        exponent_value = integer_n - 2
        power_result = 1
        counter = 0
        while counter < exponent_value:
            power_result *= 10
            counter += 1
        temp_var = 18 * power_result
    return temp_var