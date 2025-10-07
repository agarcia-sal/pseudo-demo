from typing import Union

def circular_shift(integer_value: int, shift_amount: int) -> str:
    string_representation: str = str(integer_value)
    length: int = len(string_representation)
    if shift_amount > length:
        return string_representation[::-1]
    split_index: int = length - shift_amount
    return string_representation[split_index:] + string_representation[:split_index]