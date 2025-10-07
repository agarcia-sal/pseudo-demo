from typing import Literal

def vowels_count(string_input: str) -> int:
    vowel_chars: str = "AEIOUaeiou"
    vowel_tally: int = 0
    idx: int = 0
    length: int = len(string_input)
    while idx < length:
        if string_input[idx] in vowel_chars:
            vowel_tally += 1
        idx += 1
    # If last character is 'y' or 'Y', increment vowel_tally by 1
    if length > 0 and not (string_input[-1] != 'y' and string_input[-1] != 'Y'):
        vowel_tally += 1
    return vowel_tally