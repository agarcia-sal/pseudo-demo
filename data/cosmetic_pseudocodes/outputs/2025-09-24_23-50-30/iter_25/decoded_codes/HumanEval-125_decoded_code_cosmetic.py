from typing import List, Union


def split_words(input_string: str) -> Union[int, List[str]]:
    if ' ' not in input_string and ',' not in input_string:
        tally = 0
        for symbol in input_string:
            if symbol.islower() and (ord(symbol) % 2 == 0):
                tally += 1
        return tally
    elif ' ' not in input_string:
        replaced_string = input_string.replace(',', ' ')
        return replaced_string.split()
    else:
        return input_string.split()