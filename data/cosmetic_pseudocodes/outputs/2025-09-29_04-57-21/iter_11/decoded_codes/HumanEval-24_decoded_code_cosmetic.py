def largest_divisor(integer_n: int) -> int:
    current_index: int = integer_n - 1
    while current_index > 0:
        if integer_n % current_index == 0:
            return current_index
        current_index -= 1
    # In case integer_n is 0 or 1, return 0 as no divisor other than itself exists
    return 0