from typing import List


def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    collected_groups: List[str] = []
    buffer_chars: List[str] = []
    depth_level: int = 0
    index_tracker: int = 0

    while index_tracker < len(string_of_parentheses):
        current_char: str = string_of_parentheses[index_tracker]

        if current_char == '(':
            depth_level += 1
            buffer_chars.append(current_char)
        else:
            if current_char == ')':
                depth_level -= 1
                buffer_chars.append(current_char)
                if depth_level == 0:
                    collected_groups.append(''.join(buffer_chars))
                    buffer_chars = []

        index_tracker += 1

    return collected_groups