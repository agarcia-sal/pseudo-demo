from typing import Union

def digits(n: Union[int, str]) -> int:
    result_product: int = 1
    tally_odd: int = 0
    s: str = str(n)
    index: int = 0
    length: int = len(s)
    while index < length:
        digit_val: int = int(s[index])
        if digit_val % 2 != 0:
            result_product *= digit_val
            tally_odd += 1
        index += 1
    return result_product if tally_odd != 0 else 0