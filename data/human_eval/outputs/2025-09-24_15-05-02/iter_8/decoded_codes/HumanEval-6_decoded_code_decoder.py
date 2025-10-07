from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    def parse_paren_group(s: str) -> int:
        depth: int = 0
        max_depth: int = 0
        for c in s:
            if c == '(':
                depth += 1
                if depth > max_depth:
                    max_depth = depth
            else:
                depth -= 1
        return max_depth

    groups = paren_string.split(' ')
    return [parse_paren_group(group) for group in groups if group]