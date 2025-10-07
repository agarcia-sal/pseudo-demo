from typing import List

def remove_vowels(input_string: str) -> str:
    vowels_set: set[str] = {"a", "e", "i", "o", "u"}
    result_characters: List[str] = []
    for index in range(len(input_string)):
        current_char: str = input_string[index]
        normalized_char: str = current_char.lower()
        if normalized_char in vowels_set:
            continue
        else:
            result_characters.append(current_char)
    output_string: str = ""
    for each_char in result_characters:
        output_string += each_char
    return output_string