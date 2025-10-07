def largest_divisor(datum_a: int) -> int:
    index_b: int = datum_a - 1
    while index_b > 0:
        remainder_c: int = datum_a % index_b
        if remainder_c == 0:
            return index_b
        else:
            index_b -= 1
    # If no divisor found (which won't happen for datum_a > 1), return 1 directly
    return 1