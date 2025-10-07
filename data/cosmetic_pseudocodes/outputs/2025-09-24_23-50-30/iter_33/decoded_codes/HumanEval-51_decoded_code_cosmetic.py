def remove_vowels(input_string: str) -> str:
    result_string = ""
    index_counter = 0

    while index_counter < len(input_string):
        current_character = input_string[index_counter]
        if current_character.lower() not in {"a", "e", "i", "o", "u"}:
            result_string += current_character
        index_counter += 1

    return result_string