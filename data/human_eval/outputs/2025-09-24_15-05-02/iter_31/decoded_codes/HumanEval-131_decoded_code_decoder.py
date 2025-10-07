from typing import Optional

def digits(positive_integer: int) -> int:
    if positive_integer <= 0:
        raise ValueError("Input must be a positive integer")
    product = 1
    odd_digit_count = 0
    for ch in str(positive_integer):
        digit = int(ch)
        if digit % 2 == 1:
            product *= digit
            odd_digit_count += 1
    return product if odd_digit_count > 0 else 0