from typing import Tuple

def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    filtered_builder = []
    index_counter = 0
    while index_counter < len(string_s):
        current_char = string_s[index_counter]
        if current_char not in string_c:
            filtered_builder.append(current_char)
        index_counter += 1
    processed_string = ''.join(filtered_builder)
    reversed_string = ''
    rev_index = len(processed_string) - 1
    while rev_index >= 0:
        reversed_string += processed_string[rev_index]
        rev_index -= 1
    return processed_string, reversed_string == processed_string