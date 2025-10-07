def largest_divisor(num: int) -> int:
    candidate: int = num - 1
    while candidate > 0:
        if num % candidate == 0:
            return candidate
        candidate -= 1
    # theoretically unreachable since 1 divides all integers > 0
    return 1