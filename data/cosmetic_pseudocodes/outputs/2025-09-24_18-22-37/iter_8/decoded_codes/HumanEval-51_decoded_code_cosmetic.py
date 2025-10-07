def remove_vowels(input_string: str) -> str:
    result_builder: str = ""
    character_index: int = 0
    vowels = {"a", "e", "i", "o", "u"}
    while character_index < len(input_string):
        current_character = input_string[character_index]
        lowered_character = current_character.lower()
        if lowered_character not in vowels:
            result_builder += current_character
        character_index += 1
    return result_builder