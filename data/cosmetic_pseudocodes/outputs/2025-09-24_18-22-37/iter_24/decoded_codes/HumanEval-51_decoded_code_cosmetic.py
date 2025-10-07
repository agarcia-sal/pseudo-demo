def remove_vowels(input_string: str) -> str:
    result_string = ""
    position_index = 0
    vowels = {"a", "e", "i", "o", "u"}
    while position_index < len(input_string):
        current_character = input_string[position_index]
        lowercase_character = current_character.lower()
        if lowercase_character in vowels:
            skip_character_flag = True
        else:
            skip_character_flag = False
        if not skip_character_flag:
            result_string += current_character
        position_index += 1
    return result_string