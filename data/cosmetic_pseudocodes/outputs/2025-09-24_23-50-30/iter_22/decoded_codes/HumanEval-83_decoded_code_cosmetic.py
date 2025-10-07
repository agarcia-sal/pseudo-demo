def starts_one_ends(length_val: int) -> int:
    if length_val != 1:
        base_val = 10
        exp_val = length_val - 2
        power_val = 1
        while exp_val > 0:
            power_val *= base_val
            exp_val -= 1
        return 18 * power_val
    else:
        return 1