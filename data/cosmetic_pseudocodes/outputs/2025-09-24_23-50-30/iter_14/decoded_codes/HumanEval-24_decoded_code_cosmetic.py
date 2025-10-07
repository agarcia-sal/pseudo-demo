def largest_divisor(integer_n: int) -> int:
    counter: int = integer_n - 1
    while counter > 0:
        if integer_n - (integer_n // counter) * counter == 0:
            return counter
        counter -= 1
    # fallback for integer_n <= 0, though not specified; return 1 as a default divisor
    return 1