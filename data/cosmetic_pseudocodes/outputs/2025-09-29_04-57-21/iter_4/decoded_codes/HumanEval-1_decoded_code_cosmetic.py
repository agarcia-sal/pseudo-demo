from typing import List


def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    collected_groups: List[str] = []
    temp_chars: List[str] = []
    nesting_level: int = 0
    position: int = 0

    while position < len(string_of_parentheses):
        current_char: str = string_of_parentheses[position]

        if current_char == '(':
            nesting_level += 1
            temp_chars.append(current_char)

        elif current_char == ')':
            nesting_level -= 1
            temp_chars.append(current_char)

            if nesting_level == 0:
                combined_str = ''.join(temp_chars)
                collected_groups.append(combined_str)
                temp_chars = []

        position += 1

    return collected_groups