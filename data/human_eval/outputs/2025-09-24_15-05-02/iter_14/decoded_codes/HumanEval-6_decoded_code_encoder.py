from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    def parse_paren_group(s: str) -> int:
        depth = 0
        max_depth = 0
        for character in s:
            if character == '(':
                depth += 1
                max_depth = max(depth, max_depth)
            else:
                depth -= 1
        return max_depth

    groups = paren_string.split(' ')
    result = []
    for x in groups:
        if x:
            result.append(parse_paren_group(x))
    return result