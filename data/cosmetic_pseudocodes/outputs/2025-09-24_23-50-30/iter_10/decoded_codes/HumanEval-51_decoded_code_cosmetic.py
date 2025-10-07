from typing import List

def remove_vowels(input_string: str) -> str:
    vowels_set = {"a", "e", "i", "o", "u"}
    result_characters: List[str] = []
    for each_char in input_string:
        lowercase_char = each_char
        if lowercase_char == lowercase_char.upper():
            lowercase_char = lowercase_char.lower()
        if lowercase_char not in vowels_set:
            result_characters.append(each_char)
    return "".join(result_characters)