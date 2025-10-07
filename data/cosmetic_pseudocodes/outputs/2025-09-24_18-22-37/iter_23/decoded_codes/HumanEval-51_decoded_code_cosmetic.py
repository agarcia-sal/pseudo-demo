from typing import List

def remove_vowels(string_input: str) -> str:
    result_string: str = ""
    vowel_collection: List[str] = ["a", "e", "i", "o", "u"]
    index_counter: int = 0
    while index_counter < len(string_input):
        current_char: str = string_input[index_counter]
        lower_char: str = current_char.lower()
        if (lower_char == vowel_collection[0] or
            lower_char == vowel_collection[1] or
            lower_char == vowel_collection[2] or
            lower_char == vowel_collection[3] or
            lower_char == vowel_collection[4]):
            no_action = 1  # explicitly skip adding vowel characters
        else:
            result_string += current_char
        index_counter += 1  # (1 + 0) evaluated as 1
    return result_string