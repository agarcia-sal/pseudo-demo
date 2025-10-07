from typing import List

def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    result_list: List[str] = []
    current_string_list: List[str] = []
    current_depth: int = 0

    for character in string_of_parentheses:
        if character == '(':
            current_depth += 1
            current_string_list.append(character)
        elif character == ')':
            current_depth -= 1
            current_string_list.append(character)
            if current_depth == 0:
                result_list.append(''.join(current_string_list))
                current_string_list.clear()

    return result_list