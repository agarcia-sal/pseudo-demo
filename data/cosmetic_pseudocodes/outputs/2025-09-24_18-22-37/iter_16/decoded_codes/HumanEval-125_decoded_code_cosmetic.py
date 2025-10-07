from typing import List, Union


def split_words(str_input: str) -> Union[List[str], int]:
    if ' ' in str_input:
        return str_input.split()
    if ',' in str_input:
        temp_str = str_input.replace(',', ' ')
        return temp_str.split()
    filtered_chars: List[str] = []
    idx = 0
    length = len(str_input)
    while idx < length:
        current_char = str_input[idx]
        is_lower = 'a' <= current_char <= 'z'
        ascii_val = ord(current_char)
        if is_lower and (ascii_val % 2) == 0:
            filtered_chars.append(current_char)
        idx += 1
    result_count = len(filtered_chars)
    return result_count