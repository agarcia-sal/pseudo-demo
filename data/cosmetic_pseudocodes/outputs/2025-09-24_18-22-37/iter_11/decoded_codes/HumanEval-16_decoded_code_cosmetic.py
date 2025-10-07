from typing import Set

def count_distinct_characters(input_string_param: str) -> int:
    lowercase_version: str = ""
    char_set: Set[str] = set()
    character_index: int = 0

    while character_index < len(input_string_param):
        current_character: str = input_string_param[character_index]
        lower_char: str = current_character.lower()
        lowercase_version += lower_char
        character_index += 1

    character_index = 0
    distinct_count: int = 0

    while character_index < len(lowercase_version):
        current_character = lowercase_version[character_index]
        if current_character not in char_set:
            char_set = char_set.union({current_character})
        character_index += 1

    distinct_count = len(char_set)
    return distinct_count