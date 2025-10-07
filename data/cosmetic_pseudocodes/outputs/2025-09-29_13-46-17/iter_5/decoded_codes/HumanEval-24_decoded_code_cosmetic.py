def largest_divisor(integer_n: int) -> int:
    current_value: int = integer_n - 1
    while current_value > 0:
        if integer_n % current_value == 0:
            return current_value
        current_value -= 1
    # Should never reach here for integer_n > 0 (1 always divides integer_n)
    return 1