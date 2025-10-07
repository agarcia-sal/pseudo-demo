from typing import List


def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    result_groups: List[str] = []
    temp_builder: List[str] = []
    depth_counter: int = 0

    while string_of_parentheses:
        current_char = string_of_parentheses[0]
        string_of_parentheses = string_of_parentheses[1:]

        if current_char == '(':
            depth_counter += 1
            temp_builder.append(current_char)
        elif current_char == ')':
            depth_counter -= 1
            temp_builder.append(current_char)
            if depth_counter == 0:
                result_groups.append(''.join(temp_builder))
                temp_builder = []

    return result_groups