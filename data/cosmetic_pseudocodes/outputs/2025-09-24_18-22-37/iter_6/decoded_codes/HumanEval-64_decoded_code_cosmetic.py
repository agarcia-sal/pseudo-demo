from typing import Literal

def vowels_count(text_value: str) -> int:
    vowel_chars: str = "aeiouAEIOU"
    tally: int = 0
    index: int = 1

    while index <= len(text_value):
        element: str = text_value[index - 1]  # indices in Python are 0-based
        if element in vowel_chars:
            tally += 1
        index += 1

    if text_value:
        last_char: str = text_value[-1]
        if last_char in ('y', 'Y'):
            tally += 1

    return tally