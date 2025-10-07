from typing import Literal

def remove_vowels(alpha: str) -> str:
    output: str = ""
    index: int = 0
    vowels: set[Literal['a', 'e', 'i', 'o', 'u']] = {'a', 'e', 'i', 'o', 'u'}
    while index < len(alpha):
        current_char: str = alpha[index]
        lower_char: str = current_char.lower()
        if lower_char not in vowels:
            output += current_char
        index += 1
    return output