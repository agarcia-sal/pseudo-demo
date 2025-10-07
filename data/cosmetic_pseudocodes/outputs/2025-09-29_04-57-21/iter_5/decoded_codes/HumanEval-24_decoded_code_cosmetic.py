def largest_divisor(integer_n: int) -> int:
    pointer: int = integer_n - 1
    while pointer > 0:
        if integer_n % pointer == 0:
            return pointer
        pointer -= 1
    # fallback, if no divisor found (should not happen for integer > 1)
    return 1