def greatest_common_divisor(a: int, b: int) -> int:
    # Compute the Greatest Common Divisor (GCD) using the Euclidean algorithm
    while b != 0:
        a, b = b, a % b
    return a