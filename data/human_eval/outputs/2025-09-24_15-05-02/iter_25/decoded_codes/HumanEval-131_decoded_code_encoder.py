from typing import Union

def digits(n: int) -> int:
    product: int = 1
    odd_count: int = 0
    for digit in str(abs(n)):  # handle negative numbers by considering absolute value
        int_digit: int = int(digit)
        if int_digit % 2 == 1:
            product *= int_digit
            odd_count += 1
    return product if odd_count > 0 else 0