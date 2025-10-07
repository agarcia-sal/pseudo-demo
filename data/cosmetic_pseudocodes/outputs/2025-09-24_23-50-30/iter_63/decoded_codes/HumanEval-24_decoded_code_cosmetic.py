def largest_divisor(integer_n: int) -> int:
    integer_index: int = integer_n - 1
    while integer_index > 0:
        if integer_n % integer_index == 0:
            return integer_index
        integer_index -= 1
    # For completeness; integer_n > 0 assumed, 1 divides all positive integers
    return 1