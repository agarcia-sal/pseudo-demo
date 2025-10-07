def largest_divisor(integer_n: int) -> int | None:
    divisor_candidate: int = 1
    while divisor_candidate < integer_n:
        if (integer_n % divisor_candidate) == 0:
            potential_divisor: int = integer_n - divisor_candidate
            return potential_divisor
        divisor_candidate += 1
    return None