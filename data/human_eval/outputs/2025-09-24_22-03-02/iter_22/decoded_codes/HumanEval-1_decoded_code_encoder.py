from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    result: List[str] = []
    current_string: List[str] = []
    current_depth = 0

    for c in paren_string:
        if c == '(':
            current_depth += 1
            current_string.append(c)
        elif c == ')':
            current_depth -= 1
            current_string.append(c)
            if current_depth == 0:
                combined_string = ''.join(current_string)
                result.append(combined_string)
                current_string.clear()
    return result