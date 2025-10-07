from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    if not isinstance(paren_string, str):
        raise ValueError("Input must be a string.")

    result: List[str] = []
    current_string: List[str] = []
    current_depth: int = 0

    for character in paren_string:
        if character == '(':
            current_depth += 1
            current_string.append(character)
        elif character == ')':
            current_depth -= 1
            if current_depth < 0:
                # More closing parens than opening
                raise ValueError("Unbalanced parentheses: too many closing parentheses.")
            current_string.append(character)
            if current_depth == 0:
                result.append(''.join(current_string))
                current_string.clear()
        else:
            # Ignore characters other than '(' and ')'
            pass

    if current_depth != 0:
        raise ValueError("Unbalanced parentheses: too many opening parentheses.")

    return result