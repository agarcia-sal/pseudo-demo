from typing import List, Union


def split_words(input_str: str) -> Union[List[str], int]:
    if " " in input_str:
        # Tokenize by whitespace if space present
        return input_str.split()
    elif "," in input_str:
        # Replace commas with spaces and tokenize
        tmp_str = "".join(" " if ch == "," else ch for ch in input_str)
        return tmp_str.split()
    else:
        # Filter lowercase chars with even ASCII codes and return their count
        char_list = [ch for ch in input_str if ch.islower() and (ord(ch) % 2 == 0)]
        return len(char_list)