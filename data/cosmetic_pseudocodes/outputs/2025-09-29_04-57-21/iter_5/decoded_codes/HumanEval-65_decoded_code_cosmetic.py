from typing import Union

def circular_shift(num_val: Union[int, float], shift_amt: int) -> str:
    str_form = str(num_val)
    if not (shift_amt <= len(str_form)):
        return str_form[::-1]
    split_pos = len(str_form) - shift_amt
    return str_form[split_pos:] + str_form[:split_pos]