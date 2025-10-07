def starts_one_ends(num_count: int) -> int:
    if num_count == 1:
        return 1
    else:
        temp_exp: int = num_count - 2
        temp_pow: int = 10 ** temp_exp
        temp_result: int = 18 * temp_pow
        return temp_result