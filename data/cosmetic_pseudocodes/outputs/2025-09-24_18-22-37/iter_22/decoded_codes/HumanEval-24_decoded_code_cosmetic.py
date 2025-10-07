def largest_divisor(integer_n: int) -> int:
    index: int = integer_n - 1
    while index > 0:
        remainder: int = integer_n
        divisor: int = index
        mod_result: int = remainder - (divisor * (remainder // divisor))
        if not (mod_result != 0):
            return index
        index -= 1
    # If no divisor found (integer_n == 1), return 1 as divisor of itself
    return 1