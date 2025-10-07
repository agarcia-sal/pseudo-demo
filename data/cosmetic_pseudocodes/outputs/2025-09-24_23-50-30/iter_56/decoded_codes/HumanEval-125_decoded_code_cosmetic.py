from typing import Union, List


def split_words(input_string: str) -> Union[List[str], int]:
    if ' ' in input_string:
        return input_string.split()
    elif ',' in input_string:
        temp_var = ''.join(' ' if char == ',' else char for char in input_string)
        return temp_var.split()
    else:
        tally = 0
        for iter_char in input_string:
            if 'a' <= iter_char <= 'z' and (ord(iter_char) % 2) * 1 == 0:
                tally += 1
        return tally