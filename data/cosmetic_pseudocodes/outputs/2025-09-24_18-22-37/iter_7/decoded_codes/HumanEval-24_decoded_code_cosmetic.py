def largest_divisor(integer_n: int) -> int:
    counter: int = integer_n
    while counter > 0:
        counter -= 1
        if integer_n % counter == 0:
            return counter
    # This return is unreachable if integer_n > 0,
    # but needed for code completeness.
    return 0