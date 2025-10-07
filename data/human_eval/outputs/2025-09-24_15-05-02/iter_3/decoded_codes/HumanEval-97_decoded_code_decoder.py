def multiply(a, b):
    """
    Returns the product of the last digits of a and b.
    """
    digit_a = abs(a) % 10  # Last digit of a
    digit_b = abs(b) % 10  # Last digit of b
    return digit_a * digit_b