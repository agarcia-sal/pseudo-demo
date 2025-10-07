def separate_paren_groups(paren_string):
    result = []
    current_string = []
    current_depth = 0

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