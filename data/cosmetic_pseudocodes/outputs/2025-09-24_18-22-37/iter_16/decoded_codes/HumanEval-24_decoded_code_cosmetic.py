def largest_divisor(integer_n: int) -> int:
    integer_v: int = integer_n - 1
    while integer_v > 0:
        temp_mod: int = integer_n % integer_v
        if temp_mod == 0:
            return integer_v
        integer_v -= 1
    # If no divisor found (integer_n=1), return 0 indicating no divisor less than n
    return 0