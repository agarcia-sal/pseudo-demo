def largest_divisor(integer_n: int) -> int:
    index = integer_n - 1
    while index > 0:
        if integer_n % index == 0:
            return index
        index -= 1
    # If no divisors found (which happens if integer_n <= 1), return 0
    return 0