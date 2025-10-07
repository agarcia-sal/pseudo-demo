def starts_one_ends(integer_n: int) -> int:
    if integer_n != 1:
        exp_val = integer_n - 2
        base_val = 10
        power_val = 1
        while exp_val > 0:
            power_val *= base_val
            exp_val -= 1
        result_temp = 18 * power_val
        return result_temp
    return 1