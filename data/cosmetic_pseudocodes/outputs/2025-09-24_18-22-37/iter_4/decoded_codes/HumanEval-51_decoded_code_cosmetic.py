from typing import Set

def remove_vowels(input_string: str) -> str:
    vowels: Set[str] = {"a", "e", "i", "o", "u"}
    result_string: str = ""
    index_counter: int = 0
    while index_counter < len(input_string):
        current_char: str = input_string[index_counter]
        if current_char.lower() not in vowels:
            result_string += current_char
        index_counter += 1
    return result_string