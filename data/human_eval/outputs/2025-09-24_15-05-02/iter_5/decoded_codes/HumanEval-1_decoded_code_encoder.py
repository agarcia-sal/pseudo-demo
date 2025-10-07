from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    result: List[str] = []
    current_string: List[str] = []
    current_depth: int = 0

    for char in paren_string:
        if char == '(':
            current_depth += 1
            current_string.append(char)
        elif char == ')':
            current_depth -= 1
            current_string.append(char)
            if current_depth == 0:
                result.append(''.join(current_string))
                current_string.clear()

    return result