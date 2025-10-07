from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    result_list: List[str] = []
    current_group_characters: List[str] = []
    nesting_depth: int = 0

    for character in paren_string:
        if character == '(':
            nesting_depth += 1
            current_group_characters.append(character)
        elif character == ')':
            nesting_depth -= 1
            current_group_characters.append(character)

            if nesting_depth == 0:
                group_string = ''.join(current_group_characters)
                result_list.append(group_string)
                current_group_characters.clear()
    return result_list