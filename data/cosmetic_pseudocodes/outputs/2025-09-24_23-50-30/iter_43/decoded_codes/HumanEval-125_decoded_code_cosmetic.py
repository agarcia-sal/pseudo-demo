from typing import Union, List

def split_words(input_string: str) -> Union[int, List[str]]:
    if ' ' not in input_string and ',' not in input_string:
        counter = 0
        for symbol in input_string:
            if 'a' <= symbol <= 'z' and (ord(symbol) % 2 == 0):
                counter += 1
        return counter
    if ' ' in input_string:
        return input_string.split(' ')
    if ',' in input_string:
        # Replace commas with spaces and split
        intermediate_string = ''.join(' ' if ch == ',' else ch for ch in input_string)
        return intermediate_string.split(' ')