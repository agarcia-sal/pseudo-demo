from typing import List, Union


def split_words(input_string: str) -> Union[List[str], int]:
    if " " in input_string:
        return input_string.split()
    elif "," in input_string:
        temp_string = input_string.replace(",", " ")
        return temp_string.split()
    else:
        filtered_chars = [
            char
            for char in input_string
            if char.islower() and (ord(char) & 1) == 0
        ]
        even_lowercase_count = len(filtered_chars)
        return even_lowercase_count