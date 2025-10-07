from typing import Union

def circular_shift(num_value: Union[int, float], shift_amount: int) -> str:
    str_value = str(num_value)
    len_value = len(str_value)
    if shift_amount > len_value:
        # Reverse the string by concatenating characters from end to start
        reversed_str = ""
        idx = len_value - 1
        while idx >= 0:
            reversed_str += str_value[idx]
            idx -= 1
        return reversed_str
    else:
        cut_index = len_value - shift_amount
        # Strings in Python are 0-indexed, so adjust slicing accordingly
        first_part = str_value[cut_index:]
        second_part = str_value[:cut_index]
        return first_part + second_part