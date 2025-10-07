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
            elif c == ')':
                depth -= 1
                # Defensive: depth should never be negative in well-formed input
                if depth < 0:
                    depth = 0
            else:
                # Ignore any characters other than '(' or ')'
                continue
        return max_depth

    groups: List[str] = [x for x in paren_string.split(' ') if x]
    return [parse_paren_group(x) for x in groups]