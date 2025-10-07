from typing import List


def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    result_collection: List[str] = []
    temp_chars: List[str] = []
    depth_counter: int = 0

    for index in range(len(string_of_parentheses)):
        current_char: str = string_of_parentheses[index]

        if current_char == '(':
            depth_counter += 1
            temp_chars.append(current_char)
        elif current_char == ')':
            temp_chars.append(current_char)
            depth_counter -= 1
            if depth_counter == 0:
                result_collection.append("".join(temp_chars))
                temp_chars = []

    return result_collection