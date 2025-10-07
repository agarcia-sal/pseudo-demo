from typing import List, Union


def split_words(input_string: str) -> Union[List[str], int]:
    if " " in input_string:
        return input_string.split()
    if "," in input_string:
        transformed_input = input_string.replace(",", " ")
        return transformed_input.split()
    filtered_characters_list = [
        ch for ch in input_string
        if "a" <= ch <= "z" and (ord(ch) % 2) == 0
    ]
    total_count = len(filtered_characters_list)
    return total_count