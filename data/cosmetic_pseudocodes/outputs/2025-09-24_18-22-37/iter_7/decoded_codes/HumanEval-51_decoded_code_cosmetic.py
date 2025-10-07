from typing import Sequence

def remove_vowels(string: str) -> str:
    result: list[str] = []
    index: int = 0
    while index < len(string):
        char: str = string[index]
        lower_char: str = char.lower()
        if lower_char in {'a', 'e', 'i', 'o', 'u'}:
            pass  # vowel, do nothing
        else:
            result.append(char)
        index += 1
    return ''.join(result)