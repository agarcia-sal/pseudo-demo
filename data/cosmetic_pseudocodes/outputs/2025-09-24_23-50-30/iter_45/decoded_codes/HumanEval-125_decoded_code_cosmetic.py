from typing import Union, List


def split_words(text: str) -> Union[int, List[str]]:
    found_space: bool = False
    found_comma: bool = False

    for each_char in text:
        if each_char == ' ':
            found_space = True
        elif each_char == ',':
            found_comma = True

    if found_space:
        return text.split()
    else:
        if found_comma:
            temp_str = ''.join(' ' if ch == ',' else ch for ch in text)
            return temp_str.split()
        else:
            counter = 0
            for each_char in text:
                ascii_val = ord(each_char)
                if 'a' <= each_char <= 'z' and (ascii_val % 2 == 0):
                    counter += 1
            return counter