from typing import Sequence


def vowels_count(input_sequence: Sequence[str]) -> int:
    vowel_collection = "AEIOUaeiou"
    count_vowels = 0
    pos_index = 1
    length = len(input_sequence)
    while pos_index <= length:
        if input_sequence[pos_index - 1] in vowel_collection:  # adjust for 0-based indexing
            count_vowels += 1
        pos_index += 1
    if length > 0 and (input_sequence[-1] == 'Y' or input_sequence[-1] == 'y'):
        count_vowels += 1
    return count_vowels