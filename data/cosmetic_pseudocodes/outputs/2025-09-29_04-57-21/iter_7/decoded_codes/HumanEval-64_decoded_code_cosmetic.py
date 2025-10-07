from typing import Union


def vowels_count(string_input: str) -> int:
    vowel_set = "AEIOUaeiou"
    count_vowels = 0
    idx = 0
    length = len(string_input)
    while idx < length:
        if string_input[idx] in vowel_set:
            count_vowels += 1
        idx += 1
    if length > 0 and not (string_input[-1] != 'y' and string_input[-1] != 'Y'):
        count_vowels += 1
    return count_vowels