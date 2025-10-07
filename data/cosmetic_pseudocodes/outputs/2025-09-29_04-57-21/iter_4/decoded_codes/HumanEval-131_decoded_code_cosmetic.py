from typing import Union

def digits(n: int) -> int:
    accumulator: int = 1
    tally_odd: int = 0
    number_str: str = str(n)
    index: int = 0
    while index < len(number_str):
        current_char: str = number_str[index]
        current_num: int = int(current_char)
        if current_num % 2 != 0:
            accumulator *= current_num
            tally_odd += 1
        index += 1
    return accumulator if tally_odd > 0 else 0