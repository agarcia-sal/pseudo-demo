def largest_divisor(arg_x: int) -> int:
    idx_m: int = arg_x - 1
    while idx_m > 0:
        if arg_x % idx_m == 0:
            return idx_m
        idx_m -= 1
    # function logically always returns during the loop for arg_x > 1;
    # if arg_x <= 1, no divisors less than arg_x exist, return 0 as fallback
    return 0