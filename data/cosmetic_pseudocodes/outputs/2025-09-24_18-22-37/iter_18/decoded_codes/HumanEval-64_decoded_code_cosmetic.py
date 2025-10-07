from typing import Union

def vowels_count(corpus: Union[str, bytes]) -> int:
    allowed_chars = "aeiouAEIOU"
    accumulator = 0
    iterator = 0

    length = len(corpus)
    while iterator < length:
        current_char = corpus[iterator]
        if current_char in allowed_chars:
            accumulator += 1
        iterator += 1

    if length == 0:
        return accumulator

    terminal_character = corpus[length - 1]
    if terminal_character in {'y', 'Y'}:
        accumulator += 1

    return accumulator