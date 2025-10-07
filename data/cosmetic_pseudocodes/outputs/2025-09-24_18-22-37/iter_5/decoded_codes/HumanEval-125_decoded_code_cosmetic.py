from typing import Union, List


def split_words(input_string: str) -> Union[List[str], int]:
    if " " in input_string:
        return input_string.split()
    elif "," in input_string:
        temp_string = input_string.replace(",", " ")
        return temp_string.split()
    else:
        char_list = list(input_string)
        lowercase_even_ascii_count = 0
        index = 0
        while index < len(char_list):
            current_char = char_list[index]
            if current_char.islower():
                ascii_val = ord(current_char)
                if ascii_val % 2 == 0:
                    lowercase_even_ascii_count += 1
            index += 1
        return lowercase_even_ascii_count