from typing import Union, List


def split_words(input_string: str) -> Union[List[str], int]:
    if " " in input_string:
        return input_string.split()
    elif "," in input_string:
        temp_string = ""
        idx = 0
        while idx < len(input_string):
            if input_string[idx] == ",":
                temp_string += " "
            else:
                temp_string += input_string[idx]
            idx += 1
        return temp_string.split()
    else:
        filtered_chars = []
        idx = 0
        while idx < len(input_string):
            ch = input_string[idx]
            char_code = ord(ch)
            if ch.islower():
                # (char_code mod (1+1)) == 0 means even ascii values
                if char_code % 2 == 0:
                    filtered_chars.append(ch)
            idx += 1
        lower_ascii_even_count = len(filtered_chars)
        return lower_ascii_even_count