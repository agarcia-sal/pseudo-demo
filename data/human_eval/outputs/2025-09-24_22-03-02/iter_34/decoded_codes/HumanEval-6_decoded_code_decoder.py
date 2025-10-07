from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    def parse_paren_group(s: str) -> int:
        depth = 0
        max_depth = 0
        index = 0
        while index < len(s):
            c = s[index]
            if c == '(':
                depth += 1
                if depth > max_depth:
                    max_depth = depth
            else:
                depth -= 1
            index += 1
        return max_depth

    split_groups = []
    current_string = ''
    index = 0
    length_to_parse = len(paren_string)
    while index < length_to_parse:
        current_char = paren_string[index]
        if current_char == ' ':
            if current_string:
                split_groups.append(current_string)
                current_string = ''
        else:
            current_string += current_char
        index += 1
    if current_string:
        split_groups.append(current_string)

    results = []
    for x in split_groups:
        max_depth_for_group = parse_paren_group(x)
        results.append(max_depth_for_group)

    return results