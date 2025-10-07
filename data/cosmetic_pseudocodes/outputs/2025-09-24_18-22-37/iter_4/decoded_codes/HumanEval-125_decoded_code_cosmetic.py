from typing import List, Union


def split_words(input_text: str) -> Union[List[str], int]:
    has_space: bool = False
    has_comma: bool = False
    n: int = len(input_text)
    i: int = 0

    while i < n:
        ch = input_text[i]
        if ch == ' ':
            has_space = True
            break
        elif ch == ',':
            has_comma = True
        i += 1

    if has_space:
        return input_text.split()
    else:
        if has_comma:
            char_list: List[str] = list(input_text)
            for j, c in enumerate(char_list):
                if c == ',':
                    char_list[j] = ' '
            temp_text: str = ''.join(char_list)
            return temp_text.split()
        else:
            lowercase_even_count: int = 0
            k: int = 0
            while k < n:
                ch = input_text[k]
                if 'a' <= ch <= 'z':
                    ascii_val = ord(ch)
                    if ascii_val % 2 == 0:
                        lowercase_even_count += 1
                k += 1
            return lowercase_even_count