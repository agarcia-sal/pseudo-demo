from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        depth = 0
        max_depth = 0
        for character in group_string:
            if character == '(':
                depth += 1
                if depth > max_depth:
                    max_depth = depth
            else:
                depth -= 1
        return max_depth

    groups = paren_string.split(' ')
    result: List[int] = []
    for group in groups:
        if group:
            group_depth = parse_paren_group(group)
            result.append(group_depth)
    return result