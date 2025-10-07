from typing import List


def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    results_list: List[str] = []
    buffer_chars: List[str] = []
    depth_counter: int = 0

    index_pos: int = 0
    while index_pos < len(string_of_parentheses):
        current_char = string_of_parentheses[index_pos]

        if current_char == '(':
            depth_counter += 1
            buffer_chars.append(current_char)
        elif current_char == ')':
            depth_counter -= 1
            buffer_chars.append(current_char)
            if depth_counter == 0:
                results_list.append("".join(buffer_chars))
                buffer_chars = []

        index_pos += 1

    return results_list