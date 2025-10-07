from typing import List


def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    results_collection: List[str] = []
    buffer_chars: List[str] = []
    depth_level: int = 0
    i_index: int = 0
    length_string: int = len(string_of_parentheses)

    while i_index < length_string:
        current_symbol: str = string_of_parentheses[i_index]

        if current_symbol == '(':
            depth_level += 1
            buffer_chars.append(current_symbol)
        elif current_symbol == ')':
            depth_level -= 1
            buffer_chars.append(current_symbol)
            if depth_level == 0:
                joined_string = ''.join(buffer_chars)
                results_collection.append(joined_string)
                buffer_chars.clear()
        else:
            pass  # ignore any non-parenthesis characters per pseudocode

        i_index += 1

    return results_collection