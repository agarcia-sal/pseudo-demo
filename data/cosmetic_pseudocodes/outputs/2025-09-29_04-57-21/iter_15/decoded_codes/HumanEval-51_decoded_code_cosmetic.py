from typing import Literal

def remove_vowels(text: str) -> str:
    result_string: str = ""
    position: int = 0
    vowels: set[Literal['a', 'e', 'i', 'o', 'u']] = {'a', 'e', 'i', 'o', 'u'}

    while position < len(text):
        current_char: str = text[position]
        if current_char.lower() not in vowels:
            result_string += current_char
        position += 1

    return result_string