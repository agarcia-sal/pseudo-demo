from typing import List

def remove_vowels(phrase: str) -> str:
    result_string: str = ""
    position: int = 0
    total_chars: int = len(phrase)
    while position < total_chars:
        current_char: str = phrase[position]
        low_char: str = current_char.lower()
        if low_char not in {'a', 'e', 'i', 'o', 'u'}:
            result_string += current_char
        position += 1
    return result_string