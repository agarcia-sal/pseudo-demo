from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    def parse_paren_group(s: str) -> int:
        depth = 0
        max_depth = 0
        for char in s:
            if char == '(':
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
            result.append(parse_paren_group(group))
    return result