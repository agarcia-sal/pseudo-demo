from typing import Union

def circular_shift(integer_x: int, integer_shift: int) -> str:
    string_representation = str(integer_x)
    length = len(string_representation)
    if integer_shift > length:
        return string_representation[::-1]
    split = length - integer_shift
    return string_representation[split:] + string_representation[:split]