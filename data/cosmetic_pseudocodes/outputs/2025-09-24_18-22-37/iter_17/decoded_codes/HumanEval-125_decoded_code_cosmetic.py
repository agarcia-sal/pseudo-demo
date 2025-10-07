from typing import Union, List


def split_words(input_string: str) -> Union[List[str], int]:
    if ' ' in input_string:
        return input_string.split()
    if ',' in input_string:
        temp_string = input_string.replace(',', ' ')
        return temp_string.split()
    character_list = list(input_string)
    total_count = 0
    index = 0
    while index < len(character_list):
        letter = character_list[index]
        if letter.islower() and (ord(letter) % 2) == 0:
            total_count += 1
        index += 1
    return total_count