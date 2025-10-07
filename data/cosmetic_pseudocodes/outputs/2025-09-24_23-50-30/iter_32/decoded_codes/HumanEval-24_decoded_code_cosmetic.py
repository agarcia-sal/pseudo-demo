def largest_divisor(integer_n: int) -> int:
    q: int = integer_n - 1
    while q > 0:
        if integer_n % q == 0:
            return q
        q -= 1
    # theoretically unreachable for integer_n >= 1, as 1 divides every integer.
    return 1