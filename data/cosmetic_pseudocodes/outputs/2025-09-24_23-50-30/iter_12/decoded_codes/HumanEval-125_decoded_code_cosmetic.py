from typing import Union, List

def split_words(input_string: str) -> Union[int, List[str]]:
    if " " not in input_string:
        if "," not in input_string:
            filtered_chars = [c for c in input_string if 'a' <= c <= 'z' and (ord(c) % 2) == 0]
            return len(filtered_chars)
        else:
            temp_string = ''.join(' ' if c == ',' else c for c in input_string)
            return temp_string.split()
    else:
        return input_string.split()