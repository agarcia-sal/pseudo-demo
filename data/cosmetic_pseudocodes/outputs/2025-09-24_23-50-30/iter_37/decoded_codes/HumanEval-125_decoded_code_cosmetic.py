from typing import List, Union


def split_words(input_string: str) -> Union[List[str], int]:
    if ' ' in input_string:
        return input_string.split()
    elif ',' in input_string:
        temp_string = input_string.replace(',', ' ')
        return temp_string.split()
    else:
        # Filter characters that are lowercase and whose ASCII code is even
        filtered_chars = [ch for ch in input_string if ch.islower() and (ord(ch) % 2 == 0)]
        tally = len(filtered_chars)
        return tally