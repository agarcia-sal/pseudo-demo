def largest_divisor(integer_n: int) -> int:
    candidate = integer_n - 1
    while candidate > 0:
        if integer_n % candidate == 0:
            return candidate
        candidate -= 1
    # For integer_n = 1, no divisor except 1 itself; 
    # per the logic, function returns None implicitly here if no divisor found.