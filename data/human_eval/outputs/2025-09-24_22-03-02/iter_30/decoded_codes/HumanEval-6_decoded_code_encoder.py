from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    def parse_paren_group(s: str) -> int:
        depth = max_depth = 0
        for c in s:
            if c == '(':
                depth += 1
                if depth > max_depth:
                    max_depth = depth
            else:
                depth -= 1
        return max_depth

    result = []
    groups = []
    length_string = len(paren_string)
    current_index = 0
    current_group = ''
    while current_index < length_string:
        current_char = paren_string[current_index]
        if current_char == ' ':
            if len(current_group) > 0:
                groups.append(current_group)
                current_group = ''
        else:
            current_group += current_char
        current_index += 1
    if len(current_group) > 0:
        groups.append(current_group)

    i = 0
    groups_length = len(groups)
    while i < groups_length:
        group = groups[i]
        parsed_depth = parse_paren_group(group)
        result.append(parsed_depth)
        i += 1

    return result