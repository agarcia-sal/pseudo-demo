from typing import List

def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    list_of_result_strings: List[str] = []
    list_of_characters_in_current_group: List[str] = []
    current_nesting_depth = 0

    for character in string_of_parentheses:
        if character == '(':
            current_nesting_depth += 1
            list_of_characters_in_current_group.append(character)
        elif character == ')':
            current_nesting_depth -= 1
            list_of_characters_in_current_group.append(character)
            if current_nesting_depth == 0:
                list_of_result_strings.append("".join(list_of_characters_in_current_group))
                list_of_characters_in_current_group.clear()

    return list_of_result_strings