from typing import Union

def circular_shift(value_number: Union[int, float, str], offset_amount: int) -> str:
    text_form = str(value_number)
    length_val = len(text_form)
    if offset_amount > length_val:
        # Reverse the string if offset exceeds length
        return text_form[::-1]

    split_point = length_val - offset_amount
    # Rotate string by offset_amount characters to the right
    return text_form[split_point:] + text_form[:split_point]