from typing import Union

def vowels_count(input_string: Union[str, bytes]) -> int:
    vowels: str = "aeiouAEIOU"
    number_of_vowels: int = 0
    # Ensure input_string is a string for indexing and iteration
    if not isinstance(input_string, str):
        input_string = input_string.decode(errors='ignore') if isinstance(input_string, bytes) else str(input_string)
    for character in input_string:
        if character in vowels:
            number_of_vowels += 1
    if input_string and input_string[-1] in ('y', 'Y'):
        number_of_vowels += 1
    return number_of_vowels