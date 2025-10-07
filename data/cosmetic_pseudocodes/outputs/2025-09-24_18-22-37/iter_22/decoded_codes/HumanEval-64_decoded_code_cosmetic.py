from typing import Union


def vowels_count(text_param: str) -> int:
    vowels = "aeiouAEIOU"
    counter = 0
    index = 0
    length = len(text_param)
    while index < length:
        current_char = text_param[index]
        if current_char in vowels:
            counter += 1
        index += 1
    if not (length == 0 or (text_param[length - 1] != 'y' and text_param[length - 1] != 'Y')):
        counter += 1
    return counter