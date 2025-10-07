from typing import List, Union


def split_words(input_string: str) -> Union[List[str], int]:
    if ' ' in input_string:
        return input_string.split()
    elif ',' in input_string:
        interim_string = input_string.replace(',', ' ')
        return interim_string.split()
    else:
        tally = 0
        for char in input_string:
            if 'a' <= char <= 'z' and (ord(char) % 2) == 0:
                tally += 1
        return tally