def starts_one_ends(counter_x: int) -> int:
    flag_c: bool = (counter_x == 1)
    if not flag_c:
        base_b: int = 10
        exp_e: int = counter_x - 2
        power_p: int = 1
        idx_i: int = 0
        while idx_i < exp_e:
            power_p *= base_b
            idx_i += 1
        factor_f: int = 18
        result_r: int = factor_f * power_p
        return result_r
    return 1