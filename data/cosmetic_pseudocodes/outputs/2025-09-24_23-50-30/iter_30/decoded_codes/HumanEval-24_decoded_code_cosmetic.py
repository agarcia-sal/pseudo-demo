def largest_divisor(integer_n: int) -> int:
    current_index = integer_n - 1
    while current_index > 0:
        if integer_n % current_index == 0:
            return current_index
        current_index -= 1
    # In case no divisor found, though for integer_n > 1, we always find at least 1
    return 1