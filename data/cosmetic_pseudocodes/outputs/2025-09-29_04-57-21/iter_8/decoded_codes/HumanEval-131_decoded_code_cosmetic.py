from typing import Union

def digits(n: Union[int, float]) -> int:
    product_result: int = 1
    tally_odds: int = 0
    index: int = 0
    digits_str: str = str(n)
    while index < len(digits_str):
        current_char: str = digits_str[index]
        if current_char.isdigit():  # skip non-digit characters like decimal point or sign
            numeric_value: int = int(current_char)
            if numeric_value % 2 != 0:
                product_result *= numeric_value
                tally_odds += 1
        index += 1
    if tally_odds != 0:
        return product_result
    return 0