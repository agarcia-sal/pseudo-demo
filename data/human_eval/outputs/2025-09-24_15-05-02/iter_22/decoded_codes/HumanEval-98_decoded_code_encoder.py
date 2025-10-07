from typing import Union

def count_upper(input_string: str) -> int:
    uppercase_vowel_count: int = 0
    for index in range(0, len(input_string), 2):
        if input_string[index] in "AEIOU":
            uppercase_vowel_count += 1
    return uppercase_vowel_count