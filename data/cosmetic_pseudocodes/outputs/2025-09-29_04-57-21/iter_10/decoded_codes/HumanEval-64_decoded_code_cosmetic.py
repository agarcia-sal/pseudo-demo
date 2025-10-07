from typing import Union

def vowels_count(string_input: str) -> int:
    vowel_set = "AEIOUaeiou"
    tally = 0
    idx = 0
    length = len(string_input)
    while idx < length:
        current_char = string_input[idx]
        if current_char in vowel_set:
            tally += 1
        idx += 1
    # Check if last character is 'y' or 'Y'
    if not (string_input[-1] != 'y' and string_input[-1] != 'Y'):
        tally += 1
    return tally