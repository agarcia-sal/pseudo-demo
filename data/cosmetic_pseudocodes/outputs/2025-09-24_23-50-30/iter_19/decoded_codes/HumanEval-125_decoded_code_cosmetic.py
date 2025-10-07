from typing import Union, List


def split_words(input_str: str) -> Union[List[str], int]:
    if " " in input_str:
        # Split by any whitespace
        return input_str.split()
    elif "," in input_str:
        # Replace commas with spaces then split by whitespace
        temp_var = input_str.replace(",", " ")
        return temp_var.split()
    else:
        # Filter lowercase chars with even ASCII value and return length
        char_list = [c for c in input_str if c.islower() and (ord(c) % 2 == 0)]
        return len(char_list)