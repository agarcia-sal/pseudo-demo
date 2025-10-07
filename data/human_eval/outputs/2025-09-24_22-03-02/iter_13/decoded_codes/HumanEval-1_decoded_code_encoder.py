def separate_paren_groups(paren_string: str) -> list[str]:
    result = []
    current_string = []
    current_depth = 0

    for c in paren_string:
        if c == '(':
            current_depth += 1
            current_string.append(c)
        elif c == ')':
            current_depth -= 1
            current_string.append(c)
            if current_depth == 0:
                group_string = ''.join(current_string)
                result.append(group_string)
                current_string.clear()
    return result