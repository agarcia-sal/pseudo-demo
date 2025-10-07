from typing import Sequence

def vowels_count(input_sequence: Sequence[str]) -> int:
    vowel_collection = {'a','e','i','o','u','A','E','I','O','U'}
    accumulator = 0
    index_counter = 0
    length = len(input_sequence)
    while index_counter < length:
        if input_sequence[index_counter] in vowel_collection:
            accumulator += 1
        index_counter += 1
    if length > 0 and input_sequence[-1] in {'y', 'Y'}:
        accumulator += 1
    return accumulator