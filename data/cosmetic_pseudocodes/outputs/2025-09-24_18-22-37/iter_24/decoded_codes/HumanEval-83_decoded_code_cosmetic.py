def starts_one_ends(integer_n: int) -> int:
    if integer_n != 1:
        exp_val: int = integer_n - 2
        pow_val: int = 10 ** exp_val
        flag_result: int = 18 * pow_val
    else:
        flag_result = 1
    return flag_result