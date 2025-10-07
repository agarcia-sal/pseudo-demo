from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    def parse_paren_group(string_group: str) -> int:
        depth: int = 0
        max_depth: int = 0
        for character in string_group:
            if character == '(':
                depth += 1
                max_depth = max(depth, max_depth)
            else:
                depth -= 1
        return max_depth

    groups: List[str] = paren_string.split(' ')
    result: List[int] = []
    for group in groups:
        if group:
            result.append(parse_paren_group(group))
    return result