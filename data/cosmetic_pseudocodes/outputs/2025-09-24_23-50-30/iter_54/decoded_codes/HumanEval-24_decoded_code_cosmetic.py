def largest_divisor(integer_n: int) -> int:
    stepper: int = -1
    current_value: int = integer_n - 1
    while current_value > 0:
        if integer_n % current_value == 0:
            return current_value
        current_value += stepper
    # In case integer_n <= 1, no divisor found besides itself; return 1 as a fallback
    return 1