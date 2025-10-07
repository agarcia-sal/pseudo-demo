from typing import Union, List

def split_words(input: str) -> Union[List[str], int]:
    if ' ' not in input:
        if ',' in input:
            temp_str: str = input.replace(',', ' ')
            return temp_str.split(' ')
        else:
            chars_list: List[str] = list(input)
            filtered_chars: List[str] = [ch for ch in chars_list if 'a' <= ch <= 'z' and (ord(ch) % 2) == 0]
            total_count: int = len(filtered_chars)
            return total_count
    else:
        return input.split()