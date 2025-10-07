from typing import Union, List

def split_words(input_str: str) -> Union[int, List[str]]:
    if ' ' not in input_str:
        if ',' in input_str:
            temp_str = input_str.replace(',', ' ')
            return temp_str.split()
        else:
            filtered_chars = [ch for ch in input_str if ch.islower() and (ord(ch) % 2 == 0)]
            total = len(filtered_chars)
            return total
    else:
        return input_str.split()