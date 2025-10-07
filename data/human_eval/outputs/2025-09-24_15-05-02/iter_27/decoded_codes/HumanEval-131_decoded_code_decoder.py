from typing import Union

def digits(n: Union[int, str]) -> int:
    product: int = 1
    odd_count: int = 0
    for digit_character in str(n):
        if not digit_character.isdigit():
            raise ValueError(f"Invalid digit character encountered: {digit_character}")
        int_digit: int = int(digit_character)
        if int_digit % 2 == 1:
            product *= int_digit
            odd_count += 1
    return product if odd_count > 0 else 0