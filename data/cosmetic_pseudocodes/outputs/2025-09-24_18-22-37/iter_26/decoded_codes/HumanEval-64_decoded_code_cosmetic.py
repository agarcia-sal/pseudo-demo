from typing import Literal

def vowels_count(string_input: str) -> int:
    vowels: str = "aeiouAEIOU"
    p: int = 0
    total_vowels: int = 0
    while p < len(string_input):
        current_char: str = string_input[p]
        is_vowel: bool = False
        for v in vowels:
            if current_char == v:
                is_vowel = True
                break
        if is_vowel:
            total_vowels += 1
        p += 1
    last_char_index: int = len(string_input) - 1
    if last_char_index < 0:
        return total_vowels
    last_ch: str = string_input[last_char_index]
    if last_ch in ('y', 'Y'):
        total_vowels += 1
    return total_vowels