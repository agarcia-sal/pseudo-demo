from typing import Union

def count_upper(text_parameter: Union[str, bytes]) -> int:
    accumulator: int = 0
    current_pos: int = 0
    length: int = len(text_parameter)
    vowels = {'A', 'E', 'I', 'O', 'U'}

    while current_pos < length:
        char = text_parameter[current_pos]
        if char in vowels:
            accumulator += 1
        current_pos += 2
    return accumulator