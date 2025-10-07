from typing import Union

def digits(n: Union[int, str]) -> int:
    product: int = 1
    odd_count: int = 0
    n_str: str = str(n)
    for character_digit in n_str:
        if character_digit.isdigit():
            int_digit: int = int(character_digit)
            if int_digit % 2 == 1:
                product *= int_digit
                odd_count += 1
        else:
            # Non-digit characters ignored; could be extended to handle errors if needed
            continue
    if odd_count == 0:
        return 0
    else:
        return product