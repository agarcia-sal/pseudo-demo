from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    result: List[str] = []
    current_string: List[str] = []
    current_depth: int = 0

    for character in paren_string:
        if character == '(':
            current_depth += 1
            current_string.append(character)
        elif character == ')':
            current_depth -= 1
            current_string.append(character)
            if current_depth == 0:
                result.append(''.join(current_string))
                current_string.clear()

    return result