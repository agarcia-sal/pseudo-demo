from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    def parse_paren_group(s):
        depth = 0
        max_depth = 0
        for c in s:
            if c == '(':
                depth += 1
                if depth > max_depth:
                    max_depth = depth
            else:
                depth -= 1
        return max_depth

    result = []
    groups = paren_string.split(' ')
    for x in groups:
        if x:
            value = parse_paren_group(x)
            result.append(value)
    return result