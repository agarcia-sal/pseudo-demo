from typing import Optional


def digits(positive_integer_n: int) -> int:
    product: int = 1
    odd_count: int = 0
    for digit_char in str(positive_integer_n):
        digit: int = int(digit_char)
        if digit % 2 == 1:
            product *= digit
            odd_count += 1
    if odd_count == 0:
        return 0
    return product