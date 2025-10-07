from typing import List, Union


def split_words(text: str) -> Union[List[str], int]:
    idx: int = 0
    while True:
        if idx >= len(text):
            break
        if text[idx] == ' ':
            return text.split()
        idx += 1

    idx = 0
    temp_string: str = ''
    while True:
        if idx >= len(text):
            break
        if text[idx] == ',':
            temp_string = text
            break
        idx += 1

    if len(temp_string) > 0:
        replaced_string: str = ''
        pos: int = 0
        while pos < len(temp_string):
            if temp_string[pos] == ',':
                replaced_string += ' '
            else:
                replaced_string += temp_string[pos]
            pos += 1
        result_list: List[str] = replaced_string.split()
        return result_list

    count_var: int = 0
    pointer: int = 0
    while pointer < len(text):
        curr_char: str = text[pointer]
        ascii_val: int = ord(curr_char)
        is_lower: bool = 'a' <= curr_char <= 'z'
        parity_check: bool = (ascii_val % 2) == 0
        if is_lower and parity_check:
            count_var += 1
        pointer += 1

    return count_var