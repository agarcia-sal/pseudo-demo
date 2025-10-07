from typing import Union


def vowels_count(text: str) -> int:
    permitted_chars: str = "AEIOUaeiou"
    tally: int = 0
    for index in range(len(text)):
        current_char: str = text[index]
        if current_char in permitted_chars:
            tally += 1
    terminator: str = text[-1] if text else ''
    if terminator == 'y' or terminator == 'Y':
        tally += 1
    return tally