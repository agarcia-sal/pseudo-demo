from typing import List, Union


def split_words(input_string: str) -> Union[List[str], int]:
    if " " in input_string:
        return input_string.split()
    elif "," in input_string:
        temp_string = input_string.replace(",", " ")
        return temp_string.split()
    else:
        matching_letters = 0
        for char in input_string:
            if char.islower() and (ord(char) % 2 == 0):
                matching_letters += 1
        return matching_letters