from typing import List

def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    result_collection: List[str] = []
    buffer_chars: List[str] = []
    depth_counter: int = 0

    idx: int = 0
    while idx < len(string_of_parentheses):
        current_char: str = string_of_parentheses[idx]

        if current_char == '(':
            depth_counter += 1
            buffer_chars.append(current_char)
        elif current_char == ')':
            depth_counter -= 1
            buffer_chars.append(current_char)
            if depth_counter == 0:
                result_collection.append(''.join(buffer_chars))
                buffer_chars = []

        idx += 1

    return result_collection