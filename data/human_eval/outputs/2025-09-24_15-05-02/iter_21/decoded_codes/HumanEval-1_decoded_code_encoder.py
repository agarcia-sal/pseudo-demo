from typing import List

def separate_paren_groups(parentheses_string: str) -> List[str]:
    result: List[str] = []
    current_string: List[str] = []
    current_depth: int = 0

    for character in parentheses_string:
        if character == '(':
            current_depth += 1
            current_string.append(character)
        elif character == ')':
            current_depth -= 1
            current_string.append(character)
            if current_depth == 0:
                group_string = ''.join(current_string)
                result.append(group_string)
                current_string.clear()
    return result