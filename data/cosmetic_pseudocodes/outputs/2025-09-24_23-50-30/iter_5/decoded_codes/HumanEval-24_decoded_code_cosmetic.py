def largest_divisor(integer_n: int) -> int:
    divisor_candidate: int = integer_n - 1
    while divisor_candidate > 0:
        if integer_n % divisor_candidate == 0:
            return divisor_candidate
        divisor_candidate -= 1
    # logically unreachable if integer_n > 0, but return 1 as fallback
    return 1