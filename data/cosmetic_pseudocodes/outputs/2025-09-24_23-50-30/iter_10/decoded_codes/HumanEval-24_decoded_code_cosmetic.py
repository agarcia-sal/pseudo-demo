def largest_divisor(integer_n: int) -> int:
    j: int = integer_n - 1
    while j > 0:
        if integer_n % j == 0:
            return j
        j -= 1
    return 0  # fallback, though for integer_n > 0, will always find divisor before 0