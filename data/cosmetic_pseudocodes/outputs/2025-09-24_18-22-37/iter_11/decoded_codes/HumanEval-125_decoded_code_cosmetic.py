from typing import List, Union


def split_words(input_string: str) -> Union[List[str], int]:
    # If no spaces in input_string
    if ' ' not in input_string:
        # If comma is in input_string
        if ',' in input_string:
            temp_string = input_string
            replaced_string = ""
            initialized_index = 0
            # Replace commas with spaces
            while initialized_index < len(temp_string):
                if temp_string[initialized_index] == ',':
                    replaced_string += ' '
                else:
                    replaced_string += temp_string[initialized_index]
                initialized_index += 1
            # Return split on whitespace
            return replaced_string.split()
        else:
            # If no comma and no space, temp_string is input_string, but no explicit return here,
            # fall through to matching logic (behavior as per pseudocode)
            pass
    else:
        # If spaces present, return split on whitespace immediately
        return input_string.split()

    # When input has no spaces and no commas (or no commas leads here)
    char_list: List[str] = []
    while len(input_string) > 0:
        char_list.append(input_string[0])
        input_string = input_string[1:]

    matched_count = 0
    position_index = 0
    while position_index < len(char_list):
        temp_char = char_list[position_index]
        char_ascii = ord(temp_char)
        if 'a' <= temp_char <= 'z' and (char_ascii % 2) == 0:
            matched_count += 1
        position_index += 1

    return matched_count