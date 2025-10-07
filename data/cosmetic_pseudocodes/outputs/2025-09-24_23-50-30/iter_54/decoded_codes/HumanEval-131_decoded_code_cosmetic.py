from typing import Union

def digits(input_num: Union[int, str]) -> int:
    acc_product: int = 1
    tally_odds: int = 0
    idx: int = 0
    str_n: str = str(input_num)

    while idx < len(str_n):
        current_char: str = str_n[idx]
        num_val: int = int(current_char)

        if num_val % 2 != 0:
            acc_product *= num_val
            tally_odds += 1

        idx += 1

    return 0 if tally_odds == 0 else acc_product