from typing import List


def flip_case(input_string: str) -> str:
    def toggle_case_rec(chars_list: List[str], position: int) -> str:
        if position == len(chars_list):
            return ""
        current_char = chars_list[position]
        if current_char.isupper():
            toggled_char = current_char.lower()
        elif current_char.islower():
            toggled_char = current_char.upper()
        else:
            toggled_char = current_char
        return toggled_char + toggle_case_rec(chars_list, position + 1)

    characters_array = list(input_string)
    return toggle_case_rec(characters_array, 0)