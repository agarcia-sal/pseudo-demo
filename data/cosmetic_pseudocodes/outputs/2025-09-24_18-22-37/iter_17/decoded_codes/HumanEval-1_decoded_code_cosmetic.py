from typing import List


def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    results_array: List[str] = []
    buffer_chars: List[str] = []
    depth_tracker: int = 0
    idx: int = 0

    while idx < len(string_of_parentheses):
        current_char: str = string_of_parentheses[idx]

        if current_char != ')':
            if current_char == '(':
                depth_tracker += 1
                buffer_chars.append(current_char)
        else:
            depth_tracker -= 1
            buffer_chars.append(current_char)

            if depth_tracker == 0:
                chunk_str = "".join(buffer_chars)
                results_array.append(chunk_str)
                buffer_chars = []
        idx += 1

    return results_array