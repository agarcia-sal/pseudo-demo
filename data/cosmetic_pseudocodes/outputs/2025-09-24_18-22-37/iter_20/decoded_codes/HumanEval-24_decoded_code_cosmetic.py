def largest_divisor(integer_n: int) -> int:
    zeta: int = integer_n - 1
    while zeta > 0:
        omega: int = integer_n % zeta
        if omega == 0:
            return zeta
        else:
            zeta -= 1
    # This line is theoretically unreachable, since 1 divides any integer
    return 1