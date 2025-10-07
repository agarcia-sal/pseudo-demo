from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    def parse_paren_group(paren_group_string: str) -> int:
        current_depth = 0
        maximum_depth = 0
        for character in paren_group_string:
            if character == '(':
                current_depth += 1
                maximum_depth = max(current_depth, maximum_depth)
            else:
                current_depth -= 1
        return maximum_depth

    group_strings = paren_string.split(' ')
    depth_levels: List[int] = []
    for group_string in group_strings:
        if group_string:
            depth_levels.append(parse_paren_group(group_string))

    return depth_levels