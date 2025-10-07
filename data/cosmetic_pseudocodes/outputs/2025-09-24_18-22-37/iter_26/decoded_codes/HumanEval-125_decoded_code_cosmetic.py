from typing import List, Union

def split_words(text: str) -> Union[List[str], int]:
    i_characters: int = 0
    while i_characters < len(text):
        if text[i_characters] == ' ':
            return text.split()
        i_characters += 1

    p_commas: int = 0
    while p_commas < len(text):
        if text[p_commas] == ',':
            break
        p_commas += 1

    if p_commas < len(text):
        temp_text: str = ""
        idx: int = 0
        while idx < len(text):
            if text[idx] == ',':
                temp_text += ' '
            else:
                temp_text += text[idx]
            idx += 1
        return temp_text.split()

    n_lower_even_ascii: int = 0
    pos: int = len(text) - 1
    while pos >= 0:
        character: str = text[pos]
        if 'a' <= character <= 'z' and (ord(character) % 2 == 0):
            n_lower_even_ascii += 1
        pos -= 1

    return n_lower_even_ascii