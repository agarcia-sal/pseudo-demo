from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    current_string = []
    current_depth = 0

    for character in paren_string:
        if character == '(':
            current_depth += 1
            current_string.append(character)
        elif character == ')':
            current_depth -= 1
            current_string.append(character)

            if current_depth == 0:
                result.append("".join(current_string))
                current_string.clear()

    return result