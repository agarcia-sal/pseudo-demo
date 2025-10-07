from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    def parse_paren_group(s: str) -> int:
        depth: int = 0
        max_depth: int = 0
        for c in s:
            if c == '(':
                depth += 1
                max_depth = max(depth, max_depth)
            else:
                depth -= 1
        return max_depth

    result: List[int] = []
    for x in paren_string.split(' '):
        if x:
            result.append(parse_paren_group(x))
    return result