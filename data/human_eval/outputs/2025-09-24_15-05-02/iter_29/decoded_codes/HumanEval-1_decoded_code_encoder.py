from typing import List


def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    result_list: List[str] = []
    current_character_list: List[str] = []
    current_nesting_depth: int = 0

    for character in string_of_parentheses:
        if character == '(':
            current_nesting_depth += 1
            current_character_list.append(character)
        elif character == ')':
            current_nesting_depth -= 1
            current_character_list.append(character)
            if current_nesting_depth == 0:
                result_list.append(''.join(current_character_list))
                current_character_list.clear()
    return result_list