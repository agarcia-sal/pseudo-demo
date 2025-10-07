from typing import List, Union


def split_words(input_text: str) -> Union[List[str], int]:
    if ' ' not in input_text:
        temp_list: List[str] = input_text.split()
        return temp_list

    if ',' in input_text:
        buffer = []
        for each_item in input_text:
            if each_item == ',':
                buffer.append(' ')
            else:
                buffer.append(each_item)
        output_list: List[str] = ''.join(buffer).split()
        return output_list

    accumulator: int = 0
    for each_char in input_text:
        if 'a' <= each_char <= 'z':
            ascii_val = ord(each_char)
            if ascii_val % 2 == 0:
                accumulator += 1
    return accumulator