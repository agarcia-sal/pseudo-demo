from typing import Union

def vowels_count(input_string: Union[str, bytes]) -> int:
    vowel_characters: str = "aeiouAEIOU"
    vowel_count: int = 0
    for character in input_string:
        if character in vowel_characters:
            vowel_count += 1
    if input_string and input_string[-1] in ('y', 'Y'):
        vowel_count += 1
    return vowel_count