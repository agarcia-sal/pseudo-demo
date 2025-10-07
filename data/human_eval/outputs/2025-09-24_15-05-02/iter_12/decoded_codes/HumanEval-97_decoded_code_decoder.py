def multiply(a: int, b: int) -> int:
    digit_a = abs(a % 10)
    digit_b = abs(b % 10)
    return digit_a * digit_b