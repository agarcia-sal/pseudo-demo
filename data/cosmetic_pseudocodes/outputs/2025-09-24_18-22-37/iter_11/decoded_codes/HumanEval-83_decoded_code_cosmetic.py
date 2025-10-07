def starts_one_ends(param_m: int) -> int:
    temp_flag: bool = (param_m == 1)
    if not temp_flag:
        temp_exp: int = param_m - 2
        temp_pow: int = 1
        counter_i: int = 0
        while counter_i < temp_exp:
            temp_pow *= 10
            counter_i += 1
        return 18 * temp_pow
    else:
        return 1