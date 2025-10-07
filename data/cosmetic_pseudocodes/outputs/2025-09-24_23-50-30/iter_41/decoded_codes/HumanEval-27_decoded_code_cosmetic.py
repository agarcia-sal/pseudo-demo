from typing import Callable

def flip_case(string_parameter: str) -> str:
    def toggle_character_case(char_element: str) -> str:
        if 'a' <= char_element <= 'z':
            return char_element.upper()
        if 'A' <= char_element <= 'Z':
            return char_element.lower()
        return char_element

    def recursive_flip(index_accumulator: int, accumulator_result: str) -> str:
        if index_accumulator == len(string_parameter):
            return accumulator_result
        return recursive_flip(index_accumulator + 1, accumulator_result + toggle_character_case(string_parameter[index_accumulator]))

    return recursive_flip(0, "")