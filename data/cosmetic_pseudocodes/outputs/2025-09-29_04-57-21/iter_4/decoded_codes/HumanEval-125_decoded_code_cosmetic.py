from typing import List, Union

def split_words(input_string: str) -> Union[List[str], int]:
    if ' ' in input_string:
        # tokenize by whitespace
        return input_string.split()
    elif ',' in input_string:
        replaced_string = input_string.replace(',', ' ')
        return replaced_string.split()
    else:
        filtered_chars = [c for c in input_string if c.islower() and (ord(c) % 2 == 0)]
        total = len(filtered_chars)
        return total