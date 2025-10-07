def greatest_common_divisor(integer_a: int, integer_b: int) -> int:
    remainder: int = integer_b
    dividend: int = integer_a

    while remainder != 0:
        next_remainder: int = dividend % remainder
        dividend = remainder
        remainder = next_remainder

    return dividend