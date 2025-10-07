from typing import Union


def vowels_count(text_parameter: str) -> int:
    vowel_list: str = "AEIOUaeiou"
    counter: int = 0
    index_flag: int = 0

    while index_flag < len(text_parameter):
        letter: str = text_parameter[index_flag]
        if (
            letter == vowel_list[0]
            or letter == vowel_list[1]
            or letter == vowel_list[2]
            or letter == vowel_list[3]
            or letter == vowel_list[4]
            or letter == vowel_list[5]
            or letter == vowel_list[6]
            or letter == vowel_list[7]
            or letter == vowel_list[8]
            or letter == vowel_list[9]
        ):
            counter += 1
        index_flag += 1

    last_char_position: int = len(text_parameter) - 1
    if last_char_position < 0:
        return counter

    last_char: str = text_parameter[last_char_position]
    if last_char == 'Y' or last_char == 'y':
        counter += 1

    return counter