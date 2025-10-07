from typing import Sequence, Union

def vowels_count(input_data: Union[str, Sequence[str]]) -> int:
    count_accumulator: int = 0
    vowel_set: str = "aeiouAEIOU"

    total_length: int = len(input_data)
    position: int = 0

    while position < total_length:
        character_ref: str = input_data[position]
        if character_ref in vowel_set:
            count_accumulator += 1
        position += 1

    last_char: str = input_data[total_length - 1] if total_length > 0 else ''
    # if NOT (last_char != 'y' AND last_char != 'Y') means last_char == 'y' or last_char == 'Y'
    if last_char == 'y' or last_char == 'Y':
        count_accumulator += 1

    return count_accumulator