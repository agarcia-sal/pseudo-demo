from typing import Union

def digits(integer_n: int) -> int:
    product: int = 1
    odd_digit_count: int = 0
    for character_digit in str(abs(integer_n)):
        integer_digit = int(character_digit)
        if integer_digit % 2 == 1:
            product *= integer_digit
            odd_digit_count += 1
    return product if odd_digit_count > 0 else 0